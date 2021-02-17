
class Detections:
    def __init__(self):
        self.__detections_partitioned = {}
        self.__detections = []

    def add_detection(self, machine_id, started_at, ended_at, confidence, review):
        if machine_id not in self.__detections_partitioned:
            self.__detections_partitioned[machine_id] = {}

        detection = Detection(machine_id, started_at, ended_at, confidence, review)
        self.__detections_partitioned[machine_id][ended_at] = detection
        self.__detections.append(detection)

    def get(self, machine_id, started_at):
        return self.__detections_partitioned.get(machine_id, {}).get(started_at)

    def __len__(self):
        return len(self.__detections)


class Detection:

    def __init__(self, machine_id, started_at, ended_at, confidence, review):

        self.__machine_id = machine_id
        self.__started_at = started_at
        self.__ended_at = ended_at
        self.__confidence = confidence
        self.__review = review