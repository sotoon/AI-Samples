###############################################################################
# SECTION 1: Imports
# Import the .py files you generated from the .proto file
###############################################################################
import grpc  # install using `python3 -m pip install grpcio`

from spell_checker_pb2 import CorrectRequest
from spell_checker_pb2_grpc import SpellCheckerStub

###############################################################################
# SECTION 2: API server address and headers
# Here you set the token and the service header, as explained in the
# terminology section of the repo's Readme.
###############################################################################
address = "api.ai.sotoon.ir:443"
headers = (
    ('token', "<PUT_YOUR_SERVICE_USER_TOKEN_THAT_YOU_RECEIVED_FROM_OCEAN_HERE>"),
    ('service', ""),
)

###############################################################################
# SECTION 3: Send a request
###############################################################################
def initiate_connection(address):
    channel = grpc.secure_channel(address, grpc.ssl_channel_credentials())

    return channel


def make_request(channel, headers, request):
    stub = SpellCheckerStub(channel)
    proto_response, call = stub.Correct.with_call(
        metadata=headers,
        request=request,
    )
    return proto_response


###############################################################################
# SECTION 4: Use it in your project
###############################################################################
def a_function_in_your_project():
    # doing your own stuff ...

    channel = initiate_connection(address)
    spell_checker_request = CorrectRequest(text="helo worlde")
    spell_checker_response = make_request(channel, headers, spell_checker_request)

    return spell_checker_response

###############################################################################
# Just for demonstration
###############################################################################
spell_checker_response = a_function_in_your_project()
print(spell_checker_response)
print('one sample result:', spell_checker_response.suggestions[0].suggestions[0].text)