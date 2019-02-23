# Mashup 7조 해커톤 Back-end

## Requirements

```
pipenv install
```

## Track 관련
### TrackList(Track 목록)
#### URL
`/tracks/`
#### Method
`GET`
#### Params
None
#### Result
```
[
    {
        "id": 4,
        "created_at": "2019-02-20T13:48:55.753256Z",
        "title": "첫번째 트랙",
        "track": "/media/tracks/KakaoTalk_Audio_2019-02-20-20-48-39.m4a",
        "creator": 4,
        "like_count": 1
    },
    {
        "id": 5,
        "created_at": "2019-02-22T05:01:47.793297Z",
        "title": "두번째 트랙",
        "track": "/media/tracks/KakaoTalk_Audio_2019-02-20-20-48-39_u5mNHm6.m4a",
        "creator": 4,
        "like_count": 0
    }
]
```

### TrackCreate(Track 생성)
#### URL
`/tracks/tracks/`
#### Method
`POST`
#### Params
- title
- track
#### Result
```
{
    "title": "세번째 트랙",
    "track": "/media/tracks/KakaoTalk_Audio_2019-02-20-20-48-39_u5mNHm6.m4a"
}
```
### TrackLikeCreate(TrackLike 생성)
유저는 각 track을 한번만 like 할 수 있음 
#### URL
`/tracks/:TrackId/likes/`
#### Method
`POST`
#### Params
None
#### Result
`HTTP 201 Created`

