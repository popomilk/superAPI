'''
LINE的各種訊息介面
使用方法舉例

from MessageForm import *
test = sticker_message(1,2)
line_bot_api.reply_message(event.reply_token,test)
'''

#lineAPI
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#文字訊息介面TextSendMessage 
def text_message(text1):
    message = TextSendMessage(text=text1)
    return message

#圖片訊息介面ImageSendMessage
def image_message(url1,url2):
    message = ImageSendMessage(
        original_content_url='https://example.com/original.jpg',
        preview_image_url='https://example.com/preview.jpg'
    )
    return message

#影片訊息VideoSendMessage
def vedio_message(video_url,picture_url):
    message = VideoSendMessage(
        original_content_url='https://example.com/original.mp4',
        preview_image_url='https://example.com/preview.jpg'
    )
    return message

#AudioSendMessage(音訊訊息)
def audio_message(url,during_time_ms):
    message = AudioSendMessage(
    original_content_url='https://example.com/original.m4a',
    duration=240000
)

#LocationSendMessage(位置訊息)
def Location_message(title,address,latitude,longitude):
    message = LocationSendMessage(
        title=title,
        address=address,
        latitude=latitude,
        longitude=longitude
    )
    return message

#StickerSendMessage(貼圖訊息)
def sticker_message(package_id,sticker_id):
    message = StickerSendMessage(
        package_id=package_id,
        sticker_id=sticker_id
    )
    return message
#ImagemapSendMessage(組圖訊息)
def imagemap_message(base_url,url1,text1):
    message = ImagemapSendMessage(
        base_url=base_url,
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            URIImagemapAction(
                link_uri=url1,
                area=ImagemapArea(
                    x=0, y=0, width=1040, height=1040
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message(
    image_url,title,text,
    label1,data1,
    label2,text2,
    label3,url3
):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=image_url,
            title=title,
            text=text,
            actions=[
                DatetimePickerTemplateAction(
                    label=label1,
                    data=data1,
                    mode='date',
                    initial='2018-10-25',
                    max='2018-12-31',
                    min='2018-01-01'
                ),
                MessageTemplateAction(
                    label=label2,
                    text=text2
                ),
                URITemplateAction(
                    label=label3,
                    uri=url3
                )
            ]
        )
    )
    return message


#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template(label1,label2,text0,text1,text2,data1):

    message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text=text0,
            actions=[
                PostbackTemplateAction(
                    label=label1,
                    text=text1,
                    data=data1
                ),
                MessageTemplateAction(
                    label=label2,
                    text=text2
                )
            ]
        )
    )
    return message


#旋轉木馬按鈕訊息介面

def Carousel_Template(
    pic1,pic2,
    title1,title2,
    text1,text2,
    postlabel1,postlabel2,
    posttext1,posttext2,
    postdata1,postdata2,
    messagelabel1,messagelabel2,
    messagetext1,messagetext2,
    URIlabel1,URIlabel2,
    URIuri1,URIuri2):
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item1.jpg',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageTemplateAction(
                            label='message1',
                            text='message text1'
                        ),
                        URITemplateAction(
                            label='uri1',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageTemplateAction(
                            label='message2',
                            text='message text2'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='http://example.com/2'
                        )
                    ]
                )
            ]
        )
    )
    return message


#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)

def image_carousel_message(
    image_url1,label1,text1,data1,
    image_url2,label2,text2,data2
):
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://example.com/item1.jpg',
                    action=PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://example.com/item2.jpg',
                    action=PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    )
                )
            ]
        )
    )
    return message