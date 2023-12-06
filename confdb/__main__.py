import sys
import json
import confdb
import asyncio
import argparse


async def get(G):
    result = await G.client.get(G.key)
    print(json.dumps(result, sort_keys=True, indent=4))


async def put(G):
    result = await G.client.put(G.key, G.version, sys.stdin.read().strip())
    print(json.dumps(result, sort_keys=True, indent=4))


if '__main__' == __name__:
    G = argparse.ArgumentParser()
    G.add_argument('--cert', help='certificate path')
    G.add_argument('--cacert', help='ca certificate path')
    G.add_argument('--servers', help='comma separated list of server ip:port')
    G.add_argument('--key', help='key')
    G.add_argument('--version', help='version')
    G = G.parse_args()

    G.client = confdb.Client(G.cacert, G.cert, G.servers)
    asyncio.run(put(G)) if G.version else asyncio.run(get(G))