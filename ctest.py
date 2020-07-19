from gremlin_python.driver import client, serializer
import sys
import traceback

_gremlin_cleanup_graph = "g.V().drop()"

try:
    client = client.Client("wss://tfex-cosmos-db-10578.gremlin.cosmos.azure.com:443/", "g",
                      username="/dbs/tfex-cosmos-db-10578/colls/tfex-cosmos-gremlin-graph",
                      password="gY6JPYOzEwB03i5Q2DWIatVgPhJgU18h4PMhFi8tpk2bjmeWF49aHRSRkTkrge7ri566sTXOwzUyzuJanOPJ3A==",
                      message_serializer=serializer.GraphSONSerializersV2d0()
                      )

    print("client connection made")
    print("attempting submit")

    result_set = client.submit("[1,2,3,4]")
    print(result_set.all().result())

    client.close()

    print("client closed")

except Exception as e:
    print('There was an exception: {0}'.format(e))
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)
