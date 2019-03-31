import logging

import requests
from django.core.cache import cache
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from django.conf import settings

logger = logging.getLogger(__name__)


class SsoTokenAuthentication(BaseAuthentication):
    auth = ''
    HEADER_PREFIX = "Bearer "

    def authenticate(self, request):

        self.auth = self.get_authorization_header(request)

        if len(self.auth) <= 0 or self.auth == '':
            raise exceptions.AuthenticationFailed(
                self.shape_response_sso('Invalid token header, No credentials provided.'))

        # for now we will use the old auth token for first check if not valid will check the sso token
        if self.auth != settings.SCOPE:
            self.auth = self.extract_token_from_header(self.auth)
            valid_auth = self.check_token(self.auth)

            if not valid_auth:
                raise exceptions.AuthenticationFailed(
                    self.shape_response_sso("Invalid SSO Token."))


                # get the authorization from the requested header

    def get_authorization_header(self, request):
        """
        Return request's 'HTTP_AUTHORIZATION:' header, .
        """
        auth = request.META.get('HTTP_AUTHORIZATION', b'')

        return auth

    # extract the Bearer token
    def extract_token_from_header(self, token):
        extracted_token = token[len(self.HEADER_PREFIX):len(token)]
        return extracted_token

    # hit the check_token api to check if the sso token is valid
    def check_token(self, token):
        valid_auth = False
        # get token from cache
        roles = self.get_cache_sso(token)

        if roles is not None:
            return True

        url = settings.SSO_URL + "oauth/check_token?token=" + token
        response = requests.get(url, auth=(settings.SSO_TOKEN_ADMIN, settings.SSO_TOKEN_PASSWORD))
        response = response.json()
        if 'scope' in response and type(response['scope']) is list:
            #TODO and settings.SCOPE in response['scope']
            valid_auth = True
            # cache token fro 3 days
            self.set_cache_sso(token, response['authorities'])

        return valid_auth

    def shape_response_sso(self, message, status=False):
        response_data = {
            "status": status,
            "error_code": 403,
            "message": message
        }

        return response_data

    def get_cache_sso(self, token):
        try:
            roles = cache.get(token)
            return roles
        except Exception as e:
            logger.error("get_caching_sso", e)
            return None

    def set_cache_sso(self, token, roles):
        try:
            cache.set(token, roles, timeout=259200)
        except Exception as e:
            logger.error("set_caching_sso", e)
