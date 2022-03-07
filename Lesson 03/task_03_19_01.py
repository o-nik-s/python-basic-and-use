from xml.etree.ElementTree import XMLParser

class CubeScore:
    depth = 0
    red_score = 0
    green_score = 0
    blue_score = 0

    def start(self, tag, attrib):
        '''Вызывается для каждого открывающегося тега'''
        self.depth += 1
        if attrib['color'] == 'red':
            self.red_score += self.depth
        elif attrib['color'] == 'green':
            self.green_score += self.depth
        elif attrib['color'] == 'blue':
            self.blue_score += self.depth

    def end(self, tag):
        '''Вызывается для каждого закрывающегося тега'''
        self.depth -= 1

    def close(self):
        '''Вызывется этот метод при завершении разбора XML'''
        return str(self.red_score) + ' ' + str(self.green_score) \
            + ' ' + str(self.blue_score)

target = CubeScore()
parser = XMLParser(target=target)
parser.feed(input())
print(parser.close())

# Вариант взят из документации по xml.etree.ElementTree: https://docs.python.org/3/library/xml.etree.elementtree.html#xmlparser-objects﻿