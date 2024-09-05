import { defineStore } from 'pinia'
import { ref } from 'vue'
import * as postApi from '@/api/post'

export const useBoardStore = defineStore(

  // 스토어 이름 정의
  'board',
  () => {
    const postList = ref([{
      post_id: 103,
      title: '질문이요',
      view_count: 103,
      posting_date: '2024-08-11 12:30',
    }])

    const post = ref({ post_id: '1', title: 'test', content: 'testtest', posting_date: '2021-11-23 10:11', comments: [{ comment: 'string', comment_date: '204', post_id: '7' }] })
    const newPost = ref({ title: '', content: '' })
    const newComment = ref({ post_id: '', comment: '' })

    const commentRules = [(v: string) => v.length <= 250 || '최대 250자까지 작성 가능']

    const randomName = ref(['꿈이 있는 청년', '희망을 품고 있는 청년', '가능성이 보이는 청년', '보기 드문 청년', '제육볶음 잘 볶을 것 같은 청년', '정직한 청년'])

    const getRandomIndex = (length: any) => Math.floor(Math.random() * length)

    const getRandomName = () => randomName.value[getRandomIndex(randomName.value.length)]

    const getPostList = async () => {
      try {
        const res = await postApi.getPostList()

        postList.value = res.data
      }
      catch (error) {
        console.log('getPostList error: ', error)
      }
    }

    const getPost = async (id: any) => {
      try {
        const res = await postApi.getPost(id)

        post.value = res.data
        newComment.value.post_id = post.value.post_id
      }
      catch (error) {
        console.log('getPost error: ', error)
      }
    }

    const addPost = async () => {
      try {
        await postApi.addPost(newPost.value)
        newPost.value.title = ''
        newPost.value.content = ''
      }
      catch (error) {
        console.log('addPost error: ', error)
      }
    }

    const addComment = async () => {
      try {
        await postApi.addComment(newComment.value)
        newComment.value.comment = ''
      }
      catch (error) {
        console.log('addComment error: ', error)
      }
      finally {
        getPost(newComment.value.post_id)
      }
    }

    return {
      postList,
      post,
      newPost,
      newComment,
      commentRules,
      getRandomName,
      getPost,
      addPost,
      getPostList,
      addComment,

      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: {
      paths: ['newPost'], // postList만 persist
    }, // 지속성-persistence store이 되게 설정 (Composition API)
  },
)
