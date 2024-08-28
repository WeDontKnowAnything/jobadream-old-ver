import { defineStore } from 'pinia'
import { ref } from 'vue'
import * as postApi from '@/api/post'

export const useBoardStore = defineStore(

  // 스토어 이름 정의
  'board',
  () => {
    const router = useRouter()

    const postList = ref([{
      post_id: 103,
      title: '질문이요',
      count: 103,
      posting_date: '2024-08-11 12:30',
    }])

    const post = ref({ post_id: '1', title: 'test', content: 'testtest', posting_date: '2021-11-23 10:11' })
    const newPost = ref({ title: '', content: '' })
    const newComment = ref({ post_id: '0', content: '' })

    const comments = ref([
      { content: '마 볶아 온나', comment_date: '2021-21-23 10:11' },
      { content: '아직 안 볶아 왔나', comment_date: '2021-21-23 10:11' },
      { content: '덜 볶아 졌다', comment_date: '2021-21-23 10:11' },
    ])

    const commentRules = [(v: string) => v.length <= 250 || '최대 250자까지 작성 가능']

    const randomName = ref(['꿈이 있는 청년', '희망을 품고 있는 청년', '가능성이 보이는 청년', '보기 드문 청년', '제육볶음 잘 볶을 것 같은 청년', '정직한 청년'])

    // 랜덤하게 이름을 뽑아주는 함수
    const getRandomName = () => {
      const randomIndex = Math.floor(Math.random() * randomName.value.length)

      return randomName.value[randomIndex]
    }

    const getPostList = async () => {
      try {
        const res = await postApi.getPostList()

        console.log('getPostList: ', res)
        postList.value = res.data
      }
      catch (error) {
        console.log('getPostList error: ', error)
      }
    }

    const getPost = async (id: any) => {
      try {
        const res = await postApi.getPost(id)

        console.log('getPost: ', res)
        post.value = res.data
        console.log('post: ', post.value)
      }
      catch (error) {
        console.log('getPost error: ', error)
      }
    }

    const addPost = async () => {
      try {
        await postApi.addPost(newPost.value)

        router.go(-1)
      }
      catch (error) {
        console.log('addPost error: ', error)
      }
    }

    const getComments = async (id: any) => {
      try {
        const res = await postApi.getComments(id)

        console.log('getComments: ', res)
        postList.value = res.data
      }
      catch (error) {
        console.log('getComments error: ', error)
      }
    }

    const addComment = async () => {
      try {
        await postApi.addComment(newComment.value)
        router.go(0)
      }
      catch (error) {
        console.log('addComment error: ', error)
      }
    }

    return {
      postList,
      post,
      newPost,
      comments,
      newComment,
      commentRules,
      getRandomName,
      getPost,
      addPost,
      getPostList,
      getComments,
      addComment,

      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true, // 지속성-persistence store이 되게 설정 (Composition API)
  },
)
