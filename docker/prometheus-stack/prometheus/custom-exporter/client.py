from prometheus_client import Summary, start_http_server

test_summary = Summary("test_ms", "", ["endpoint", "parameter1", "parameter2", "parameter3"])

class ElapsedTime:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.time = time.time() - self.start

def main(id):

    with ElapsedTime() as et:
        time.sleep(5)

    endpoint = 'test'
    param1 = 1
    param2 = 2
    param3 = 3

    test_summary.labels(endpoint, param1, param2, param3).observe(et.time)

if __name__ == "__main__":

    start_http_server(8080, addr="0.0.0.0")

    num_thread = 1

    threads = []
    for thread_id in range(num_thread):
        thread = threading.Thread(target=main, args=(thread_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()