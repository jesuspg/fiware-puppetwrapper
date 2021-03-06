__author__ = 'arobres'


#REQUEST PARAMETERS
CONTENT_TYPE = u'content-type'
CONTENT_TYPE_JSON = u'application/json'
CONTENT_TYPE_XML = u'application/xml'
ACCEPT_HEADER = u'Accept'
ACCEPT_HEADER_XML = u'application/xml'
ACCEPT_HEADER_JSON = u'application/json'

AUTH_TOKEN_HEADER = u'X-Auth-Token'
TENANT_ID_HEADER = u'Tenant-Id'

HEADERS = {'content-type': CONTENT_TYPE_JSON}

#AUTHENTICATION CONSTANTS
AUTH = u'auth'
AUTH_TENANT_NAME = u'tenantName'
AUTH_PASSWORD_CREDENTIALS = u'passwordCredentials'
AUTH_USERNAME = u'username'
AUTH_PASSWORD = u'password'
AUTH_ACCESS = u'access'
AUTH_TOKEN = u'token'
AUTH_TENANT = u'tenant'
AUTH_ID = u'id'

#PUPPET PARAMETERS

PUPPET_MASTER_PATH = u'/etc/puppet/'
PUPPET_MASTER_MODULES = PUPPET_MASTER_PATH + u'modules/'
PUPPET_MASTER_MANIFESTS = PUPPET_MASTER_PATH + u'manifests/'
PUPPET_MASTER_SITE = PUPPET_MASTER_MANIFESTS + u'site.pp'
PUPPET_MASTER_SPECIFIC_MANIFEST = PUPPET_MASTER_MANIFESTS + u'{}/{}.pp'
PUPPET_MASTER_SPECIFIC_MODULE = PUPPET_MASTER_MODULES + u'{}/manifests'
SITE_PP_TEXT = u"import '{}/*.pp'"

#INSTALL / UNINSTALL / GENERATE BODYS

INSTALL_NODE_NAME = u'id'
INSTALL_GROUP_NAME = u'groupName'
INSTALL_MANIFEST_GENERATED = u'manifestGenerated'
INSTALL_ATTRIBUTES = u'attributes'
OP_SOFTWARE_LIST = u'softwareList'
OP_SOFTWARE_NAME = u'name'

#ACTIONS

INSTALL = u'INSTALL'
UNINSTALL = u'UNINSTALL'

#GENERATE CONSTANTS

ACTION = u'action'
SOFTWARE_NAME = u'softwareName'
VERSION = u'version'
GROUP = u'group'

#DOWNLOAD CONSTANTS

URL = u'URL'
MODULE_NAME = u'module_name'
REPOSITORY = u'repository'

#FABRIC CONSTANT

FABRIC_RESULT_EXECUTE = u'<local-only>'

