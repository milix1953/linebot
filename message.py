#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot.models import *


#菜單按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則菜單按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/LqBkxjV.jpg',
                    title='清蒸鱈魚 $350',
                    text='急速低溫直送鱈魚片，使用一級醬汁及白醋和些許調味料製成。肉質柔軟細嫩',
                    actions=[
                        PostbackTemplateAction(
                            label='加入菜單',
                            data='新增菜單:清蒸鱈魚'
                        ),
                        PostbackTemplateAction(
                            label='移出菜單',
                            data='刪除菜單:清蒸鱈魚'
                        ),
                        MessageTemplateAction(
                            label='查看我的菜單',
                            text='查看我的菜單'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/09YTbOs.jpg',
                    title='鐵板牛柳 $250',
                    text='嚴選牛肉上等部位，採用鐵板炙燒的方式，使牛肉帶有強烈香氣',
                    actions=[
                        PostbackTemplateAction(
                            label='加入菜單',
                            data='新增菜單:鐵板牛柳'
                        ),
                        PostbackTemplateAction(
                            label='移出菜單',
                            data='刪除菜單:鐵板牛柳'
                        ),
                        MessageTemplateAction(
                            label='查看我的菜單',
                            text='查看我的菜單'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/vGrPHVB.jpg',
                    title='鳳梨蝦球 $150',
                    text='經典台式菜餚，絕對要嘗試蝦球配上美乃滋的絕佳風味!',
                    actions=[
                        PostbackTemplateAction(
                            label='加入菜單',
                            data='新增菜單:鳳梨蝦球'
                        ),
                        PostbackTemplateAction(
                            label='移出菜單',
                            data='刪除菜單:鳳梨蝦球'
                        ),
                        MessageTemplateAction(
                            label='查看我的菜單',
                            text='查看我的菜單'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/hsv3ksi.jpg',
                    title='蝦仁滑蛋 $320',
                    text='入口即化的滑蛋，配上緊緻扎實口感的蝦仁，最後再以蔥花將味道提升到極致',
                    actions=[
                        PostbackTemplateAction(
                            label='加入菜單',
                            data='新增菜單:蝦仁滑蛋'
                        ),
                        PostbackTemplateAction(
                            label='移出菜單',
                            data='刪除菜單:蝦仁滑蛋'
                        ),
                        MessageTemplateAction(
                            label='查看我的菜單',
                            text='查看我的菜單'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/rSPVnH6.jpg',
                    title='蒜泥白肉 $200',
                    text='將白肉沾上一點蒜泥醬，兩者味道完美的結合在一起，而不再只是一塊單調的白肉',
                    actions=[
                        PostbackTemplateAction(
                            label='加入菜單',
                            data='新增菜單:蒜泥白肉'
                        ),
                        PostbackTemplateAction(
                            label='移出菜單',
                            data='刪除菜單:蒜泥白肉'
                        ),
                        MessageTemplateAction(
                            label='查看我的菜單',
                            text='查看我的菜單'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/UsIuog4.jpg',
                    title='老皮嫩肉 $220',
                    text='金黃色澤的外皮，搭上外酥內軟的口感，讓人一口接一口而欲罷不能',
                    actions=[
                        PostbackTemplateAction(
                            label='加入菜單',
                            data='新增菜單:老皮嫩肉'
                        ),
                        PostbackTemplateAction(
                            label='移出菜單',
                            data='刪除菜單:老皮嫩肉'
                        ),
                        MessageTemplateAction(
                            label='查看我的菜單',
                            text='查看我的菜單'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/hg63JXp.png',
                    title='糖醋里肌 $200',
                    text='先將里肌肉炸熟後，搭上糖醋醬再次回炸，酸酸甜甜的糖醋醬讓里肌肉增加不少風味',
                    actions=[
                        PostbackTemplateAction(
                            label='加入菜單',
                            data='新增菜單:糖醋里肌'
                        ),
                        PostbackTemplateAction(
                            label='移出菜單',
                            data='刪除菜單:糖醋里肌'
                        ),
                        MessageTemplateAction(
                            label='查看我的菜單',
                            text='查看我的菜單'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/DQlW00U.jpg',
                    title='焗烤白菜 $250',
                    text='以焗烤方式在白菜上增加不同的口感，同時在味道上也有更豐富的層次',
                    actions=[
                        PostbackTemplateAction(
                            label='加入菜單',
                            data='新增菜單:焗烤白菜'
                        ),
                        PostbackTemplateAction(
                            label='移出菜單',
                            data='刪除菜單:焗烤白菜'
                        ),
                        MessageTemplateAction(
                            label='查看我的菜單',
                            text='查看我的菜單'
                        )
                    ]
                )

            ]
        )
    )
    return message


#關於LINEBOT聊天內容範例
