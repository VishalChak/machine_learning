from lxml import html 
import pprint


class QuoraParser():
                def __init__(self,filepath,filename):
                                f = open(filepath+"/"+filename,'r+')
                                self.tags = html.fromstring(f.read())
                                f.close()
                def getLinks(self):
                                return self.tags.xpath('//div[@class="layout_2col_side"]//li[@class="related_question"]//a/@href')

                def getMainQuestion(self):
                return " ".join(self.tags.xpath('//h1//span[@class="rendered_qtext"]//text()'))
        def getAnswers(self):
                                l = len(self.tags.xpath('//div[@class="layout_2col_main"]//div[@class="AnswerListDiv"]//div[@class="pagedlist_item"]/@class'))
                                i = 1
                                ansDetails = []
                                while (i<=l):
                                                singleAnswer = self.tags.xpath('//div[@class="layout_2col_main"]//div[@class="AnswerListDiv"]//div[@class="pagedlist_item"][{0}]//div[@class="Answer AnswerBase"]//span[@class="rendered_qtext"]//text()'.format(i))
                                                views = self.tags.xpath('//div[@class="layout_2col_main"]//div[@class="AnswerListDiv"]//div[@class="pagedlist_item"][{0}]//div[@class="Answer AnswerBase"]//span[@class="meta_num"]//text()'.format(i))
                                if len(singleAnswer) < 1:
                                                                i+=1
                                                                continue
                                                ansDetails.append((" ".join(singleAnswer)," ".join(views)))
                                i+=1
                                return ansDetails
                
                def getQuestionTags(self):
                                return self.tags.xpath('//div[@class="layout_2col_main"]//span[@class="TopicNameSpan TopicName"]//text()')


if __name__ =="__main__":
                qp=QuoraParser('data/2017/3/25/6028/22','quora_6028_22_4_33_1.html')
                qp.getQuestionTags()
