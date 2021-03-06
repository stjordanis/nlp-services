import path_setup
import grpc
from services.service_spec import named_entity_recognition_rpc_pb2_grpc as grpc_bt_grpc
from services.service_spec import named_entity_recognition_rpc_pb2 as grpc_bt_pb2
from services import registry
from test_data import b64_sentences
from log import log_config

logger = log_config.getLogger('test_service.py')
channel = None

if __name__ == '__main__':

    try:
        logger.debug('call => __name == __main__')
        logger.debug("call => Creating channel() Starting... ")
        endpoint = 'localhost:{}'.format(registry['named_entity_recognition']['grpc'])
        # Open a gRPC channel
        channel = grpc.insecure_channel('{}'.format(endpoint))

    except Exception as e:
        logger.debug("Error found Creating Channel => " + e)

    try:
        logger.debug("call => RecognizeMessage() Method Test Starting... ")
        # RecognizeMessage() Method Test
        # create a stub (client)
        stub = grpc_bt_grpc.RecognizeMessageStub(channel)
        # create a valid request message
        test_data = b64_sentences.senteces()
        message = grpc_bt_pb2.InputMessage(value=test_data)
        # make the call
        response = stub.Recognize(message)
        logger.debug("call => RecognizeMessage() Method Test Passed => " + response.value)
        print()

    except Exception as e:
        logger.debug(e)

path_setup.clean_paths()
