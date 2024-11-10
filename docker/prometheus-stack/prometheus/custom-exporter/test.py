from prometheus_api_client import PrometheusConnect
import time

def test():
    prometheus_url='http://localhost:9090'
    prom = PrometheusConnect(url=prometheus_url, disable_ssl=True)

    metric_list = prom.all_metrics()

    while True:
        print()
        status = prom.get_current_metric_value('up')

        if status:
            for m in metric_list:
                if 'test' in m:
                    print('metrics name: ', m)
                    result = prom.get_current_metric_value(m)
                    print(result[0])

        else:
            print("No data available")

        time.sleep(1)

if __name__=='__main__':
    test()