from collections import deque

"""
MLFQ (Çok Seviyeli Geri Bildirim Kuyruğu)
https://en.wikipedia.org/wiki/Multilevel_feedback_queue
MLFQ, birden fazla kuyruk içerir ve her kuyruk farklı önceliklere sahiptir.

Organizatör: K. Umut Araz
Github: https://github.com/arazumut
"""



class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int) -> None:
        self.process_name = process_name  # Sürecin adı
        self.arrival_time = arrival_time  # Sürecin varış zamanı
        self.stop_time = arrival_time  # Sürecin tamamlanma zamanı veya son kesinti zamanı
        self.burst_time = burst_time  # Kalan işlem süresi
        self.waiting_time = 0  # Sürecin hazır kuyruğunda bekleme süresi
        self.turnaround_time = 0  # Varış zamanından tamamlanma zamanına kadar geçen süre


class MLFQ:
    """
    MLFQ (Çok Seviyeli Geri Bildirim Kuyruğu)
    https://en.wikipedia.org/wiki/Multilevel_feedback_queue
    MLFQ, farklı önceliklere sahip birçok kuyruk içerir.
    Bu MLFQ'de,
    İlk Kuyruk (0) ile son ikinci Kuyruk (N-2) arasında Yuvarlak Robin Algoritması uygulanır.
    Son Kuyruk (N-1) ise İlk Gelen İlk Hizmet (FCFS) algoritmasını kullanır.
    """

    def __init__(
        self,
        number_of_queues: int,
        time_slices: list[int],
        queue: deque[Process],
        current_time: int,
    ) -> None:
        self.number_of_queues = number_of_queues  # MLFQ'nin toplam kuyruk sayısı
        self.time_slices = time_slices  # Yuvarlak Robin algoritmasının uygulandığı kuyrukların zaman dilimleri
        self.ready_queue = queue  # Tamamlanmamış süreçlerin bulunduğu hazır kuyruk
        self.current_time = current_time  # Mevcut zaman
        self.finish_queue: deque[Process] = deque()  # Tamamlanan süreçlerin bulunduğu kuyruk

    def calculate_sequence_of_finish_queue(self) -> list[str]:
        """
        Bu metod, tamamlanan süreçlerin sırasını döndürür.
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P2', 'P4', 'P1', 'P3']
        """
        return [process.process_name for process in self.finish_queue]

    def calculate_waiting_time(self, queue: list[Process]) -> list[int]:
        """
        Bu metod, süreçlerin bekleme sürelerini hesaplar.
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_waiting_time([P1, P2, P3, P4])
        [83, 17, 94, 101]
        """
        return [process.waiting_time for process in queue]

    def calculate_turnaround_time(self, queue: list[Process]) -> list[int]:
        """
        Bu metod, süreçlerin dönüş sürelerini hesaplar.
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_turnaround_time([P1, P2, P3, P4])
        [136, 34, 162, 125]
        """
        return [process.turnaround_time for process in queue]

    def calculate_completion_time(self, queue: list[Process]) -> list[int]:
        """
        Bu metod, süreçlerin tamamlanma sürelerini hesaplar.
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_completion_time([P1, P2, P3, P4])
        [136, 34, 162, 125]
        """
        return [process.stop_time for process in queue]

    def calculate_remaining_burst_time_of_processes(
        self, queue: deque[Process]
    ) -> list[int]:
        """
        Bu metod, süreçlerin kalan işlem sürelerini hesaplar.
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> finish_queue, ready_queue = mlfq.round_robin(deque([P1, P2, P3, P4]), 17)
        >>> mlfq.calculate_remaining_burst_time_of_processes(mlfq.finish_queue)
        [0]
        >>> mlfq.calculate_remaining_burst_time_of_processes(ready_queue)
        [36, 51, 7]
        >>> finish_queue, ready_queue = mlfq.round_robin(ready_queue, 25)
        >>> mlfq.calculate_remaining_burst_time_of_processes(mlfq.finish_queue)
        [0, 0]
        >>> mlfq.calculate_remaining_burst_time_of_processes(ready_queue)
        [11, 26]
        """
        return [process.burst_time for process in queue]

    def update_waiting_time(self, process: Process) -> int:
        """
        Bu metod, tamamlanmamış süreçlerin bekleme sürelerini günceller.
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> mlfq.current_time = 10
        >>> P1.stop_time = 5
        >>> mlfq.update_waiting_time(P1)
        5
        """
        process.waiting_time += self.current_time - process.stop_time
        return process.waiting_time

    def first_come_first_served(self, ready_queue: deque[Process]) -> deque[Process]:
        """
        FCFS (İlk Gelen İlk Hizmet)
        FCFS, MLFQ'nin son kuyruğuna uygulanacaktır.
        İlk gelen süreç, ilk olarak tamamlanacaktır.
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.first_come_first_served(mlfq.ready_queue)
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P1', 'P2', 'P3', 'P4']
        """
        finished: deque[Process] = deque()  # Tamamlanan süreçlerin sıralı kuyruğu
        while ready_queue:
            cp = ready_queue.popleft()  # Mevcut süreç

            # Sürecin varış zamanı mevcut zamandan sonra ise, mevcut zamanı güncelle
            if self.current_time < cp.arrival_time:
                self.current_time = cp.arrival_time

            # Mevcut sürecin bekleme zamanını güncelle
            self.update_waiting_time(cp)
            # Mevcut zamanı güncelle
            self.current_time += cp.burst_time
            # Süreci tamamla ve sürecin işlem süresini 0 olarak ayarla
            cp.burst_time = 0
            # Sürecin dönüş zamanını ayarla çünkü tamamlandı
            cp.turnaround_time = self.current_time - cp.arrival_time
            # Tamamlanma zamanını ayarla
            cp.stop_time = self.current_time
            # Süreci tamamlanan süreçler kuyruğuna ekle
            finished.append(cp)

        self.finish_queue.extend(finished)  # Tamamlanan süreçleri bitiş kuyruğuna ekle
        return finished  # FCFS, tüm kalan süreçleri tamamlayacaktır

    def round_robin(
        self, ready_queue: deque[Process], time_slice: int
    ) -> tuple[deque[Process], deque[Process]]:
        """
        RR (Yuvarlak Robin)
        RR, MLFQ'nin son kuyruğu hariç tüm kuyruklarına uygulanacaktır.
        Tüm süreçler, zaman diliminden daha fazla CPU kullanamaz.
        Süreç zaman dilimini tüketirse, hazır kuyruğa geri dönecektir.
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> finish_queue, ready_queue = mlfq.round_robin(mlfq.ready_queue, 17)
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P2']
        """
        finished: deque[Process] = deque()  # Tamamlanan süreçlerin sıralı kuyruğu
        for _ in range(len(ready_queue)):  # Sadece 1 döngü için ve tamamlanmamış süreçler kuyruğa geri dönecek
            cp = ready_queue.popleft()  # Mevcut süreç

            # Sürecin varış zamanı mevcut zamandan sonra ise, mevcut zamanı güncelle
            if self.current_time < cp.arrival_time:
                self.current_time = cp.arrival_time

            # Tamamlanmamış süreçlerin bekleme zamanını güncelle
            self.update_waiting_time(cp)
            # Sürecin işlem süresi zaman diliminden büyükse
            if cp.burst_time > time_slice:
                # CPU'yu sadece zaman dilimi kadar kullan
                self.current_time += time_slice
                # Kalan işlem süresini güncelle
                cp.burst_time -= time_slice
                # Bitiş zamanını güncelle
                cp.stop_time = self.current_time
                # Süreci kuyruğun arkasına yerleştir çünkü tamamlanmadı
                ready_queue.append(cp)
            else:
                # CPU'yu kalan işlem süresi kadar kullan
                self.current_time += cp.burst_time
                # Sürecin işlem süresini 0 olarak ayarla çünkü tamamlandı
                cp.burst_time = 0
                # Bitiş zamanını ayarla
                cp.stop_time = self.current_time
                # Sürecin dönüş zamanını güncelle çünkü tamamlandı
                cp.turnaround_time = self.current_time - cp.arrival_time
                # Süreci tamamlanan süreçler kuyruğuna ekle
                finished.append(cp)

        self.finish_queue.extend(finished)  # Tamamlanan süreçleri bitiş kuyruğuna ekle
        return finished, ready_queue  # Tamamlanan süreçler kuyruğunu ve kalan süreçler kuyruğunu döndür

    def multi_level_feedback_queue(self) -> deque[Process]:
        """
        MLFQ (Çok Seviyeli Geri Bildirim Kuyruğu)
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> finish_queue = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P2', 'P4', 'P1', 'P3']
        """

        # Son kuyruk hariç tüm kuyruklar yuvarlak robin algoritmasını kullanır
        for i in range(self.number_of_queues - 1):
            finished, self.ready_queue = self.round_robin(
                self.ready_queue, self.time_slices[i]
            )
        # Son kuyruk, ilk gelen ilk hizmet algoritmasını kullanır
        self.first_come_first_served(self.ready_queue)

        return self.finish_queue


if __name__ == "__main__":
    import doctest

    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    number_of_queues = 3
    time_slices = [17, 25]
    queue = deque([P1, P2, P3, P4])

    if len(time_slices) != number_of_queues - 1:
        raise SystemExit(0)

    doctest.testmod(extraglobs={"queue": deque([P1, P2, P3, P4])})

    mlfq = MLFQ(number_of_queues, time_slices, queue, 0)
    finish_queue = mlfq.multi_level_feedback_queue()

    # Süreçlerin toplam bekleme sürelerini yazdır
    print(
        f"Bekleme süresi:\
        \t\t\t{mlfq.calculate_waiting_time([P1, P2, P3, P4])}"
    )
    # Süreçlerin tamamlanma sürelerini yazdır
    print(
        f"Tamamlanma süresi:\
        \t\t{mlfq.calculate_completion_time([P1, P2, P3, P4])}"
    )
    # Süreçlerin toplam dönüş sürelerini yazdır
    print(
        f"Dönüş süresi:\
        \t\t{mlfq.calculate_turnaround_time([P1, P2, P3, P4])}"
    )
    # Tamamlanan süreçlerin sırasını yazdır
    print(
        f"Tamamlanan süreçlerin sırası:\
        {mlfq.calculate_sequence_of_finish_queue()}"
    )
