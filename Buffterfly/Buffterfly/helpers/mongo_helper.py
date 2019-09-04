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
    def insertMaxSizeTopic(maxTopic):
        mongodb.settings.update({"key": "MAX_SIZE"}, {
                                "$set": {'value': maxTopic}},
                                upsert=True)

    @staticmethod
    def getCurrentTopicSize():
        currentSize = mongodb.settings.find_one({"key": "CURRENT_SIZE"})
        return 0 if currentSize is None else currentSize
