from pyzabbix import ZabbixAPI
from config import *


# Create ZabbixAPI class instance

class Zabbix:

    def __init__(self):
        try:

            self.zapi = ZabbixAPI(URL)
            self.zapi.login(api_token=TOKEN_ZABBIX)
            print(f"Conectado na API com Sucesso")
            print(f"Versao da API {self.zapi.api_version()}")


        except Exception as erro:

            print("Erro ao Conectar a API")
            print(f"O seguinte erro foi gerado {erro}")

    def get_hosts(self):

        hosts = self.zapi.host.get(output=[
            "hostid",
            "host",
        ], selectInterfaces=[
            "ip",
            "available",
            "error"
        ])
        return hosts

    def verify_hosts(self):

        hosts = self.get_hosts()
        hostsup = []
        hostsdown = []

        for i in hosts:

            if i['interfaces'][0]['available'] == '1':
                hostsup.append(i)

            elif i['interfaces'][0]['available'] == '2':
                hostsdown.append(i)

        return hostsup, hostsdown

    def item_get_hosts_up(self):

        cont = 0
        hostsup, null = self.verify_hosts()  # null é o hostsdown só que nao é usado nessa função
        listhostinfo = []

        for i in hostsup:

            listhostinfo.append([hostsup[cont]["host"]])

            frequency = self.zapi.item.get(output="extend",
                                           hostids=hostsup[cont]["hostid"],
                                           search={
                                               "key_": "Frequencia"
                                           })
            ssid = self.zapi.item.get(output="extend",
                                      hostids=hostsup[cont]["hostid"],
                                      search={
                                          "key_": "SSID"
                                      })

            ip = hostsup[cont]["interfaces"][0]["ip"]

            stationconnected = self.zapi.item.get(output="extend",
                                                  hostids=hostsup[cont]["hostid"],
                                                  search={
                                                      "key_": "Est.Con"
                                                  })
            try:
                listhostinfo[cont].append(ssid[0]['lastvalue'])
                listhostinfo[cont].append(frequency[0]['lastvalue'])
                listhostinfo[cont].append(ip)
                listhostinfo[cont].append(stationconnected[0]['lastvalue'])
                # print(f"Host {listhostinfo[cont]}")
                # print(f"SSID: {ssid[0]['lastvalue']}")
                # print(f"Frequencia: {frequency[0]['lastvalue']}")
                # print(f"Estacoes Conectadas: {stationconnected[0]['lastvalue']}")

            except IndexError:
                pass

            cont += 1
        print(listhostinfo)

        return listhostinfo

    def item_get_hosts_down(self):

        cont = 0
        null, hostsdown = self.verify_hosts()  # null é o hostsup só que nao é usado nessa função
        listhostinfo = []

        for i in hostsdown:

            listhostinfo.append([hostsdown[cont]["host"]])

            frequency = self.zapi.item.get(output="extend",
                                           hostids=hostsdown[cont]["hostid"],
                                           search={
                                               "key_": "Frequencia"
                                           })
            ssid = self.zapi.item.get(output="extend",
                                      hostids=hostsdown[cont]["hostid"],
                                      search={
                                          "key_": "SSID"
                                      })

            ip = hostsdown[cont]["interfaces"][0]["ip"]

            stationconnected = self.zapi.item.get(output="extend",
                                                  hostids=hostsdown[cont]["hostid"],
                                                  search={
                                                      "key_": "Est.Con"
                                                  })

            try:
                listhostinfo[cont].append(ssid[0]['lastvalue'])
                listhostinfo[cont].append(frequency[0]['lastvalue'])
                listhostinfo[cont].append(ip)
                listhostinfo[cont].append(stationconnected[0]['lastvalue'])
                # print(f"SSID: {ssid[0]['lastvalue']}")
                # print(f"Frequencia: {frequency[0]['lastvalue']}")
                # print(f"Estacoes Conectadas: {stationconnected[0]['lastvalue']}")

            except IndexError:
                pass

            cont += 1

        return listhostinfo
