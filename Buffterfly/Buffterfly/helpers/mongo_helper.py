from ..items import TopicItem
from .. import mongodb


class DBHelper:
    @staticmethod
    def insertTopic(topicItem):
        mongodb.topics.insert_one({
            'name': topicItem['name'],
            'avatar': topicItem['avatar'],
            'url': topicItem['url']
        })

    @staticmethod
    def insertImagesToTopic(detailItem):
        mongodb.topics.update({"url": detailItem['url']}, {
            "$set": {'images': detailItem['images']}},
            upsert=True)

    @staticmethod
    def insertMaxSizeTopic(maxTopic):
        mongodb.settings.update({"key": "MAX_SIZE"}, {
                                "$set": {'value': maxTopic}},
                                upsert=True)

    @staticmethod
    def getCurrentTopicSize():
        currentSize = mongodb.settings.find_one({"key": "CURRENT_SIZE"})
        return 0 if currentSize is None else int(currentSize["value"])

    @staticmethod
    def getMaxSizeTopic():
        maxSize = mongodb.settings.find_one({"key": "MAX_SIZE"})
        return 0 if maxSize is None else int(maxSize["value"])

    @staticmethod
    def updateCurrentSize(currentSize):
        mongodb.settings.update({"key": "CURRENT_SIZE"}, {
                                "$set": {'value': currentSize}},
                                upsert=True)

    @staticmethod
    def updateCurrentSizeByAddingLoadedTopic(loadedSize):
        mongodb.settings.update({"key": "CURRENT_SIZE"}, {
                                "$inc": {'value': loadedSize}})
