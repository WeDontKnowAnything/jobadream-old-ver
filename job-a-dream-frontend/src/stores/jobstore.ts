import { defineStore } from 'pinia'
import { ref } from 'vue'
import * as jobApi from '@/api/job'

export const useJobStore = defineStore(

  // 스토어 이름 정의
  'job',
  () => {
    // 객체, 함수 선언 스코프
    const job = ref('')

    const jobList = ref([{
      corp_name: 'Toss',
      title: 'NLP Engineer, 생성형 AI',
      position: '기획',
      location: '서울',
      experience_type: '신입',
      job_url: [{ platform_name: '사람인', icon: 'tabler-circle-letter-s', url: 'https://...' }, { platform_name: '사람인', icon: 'tabler-circle-letter-s', url: 'https://...' }, { platform_name: '사람인', icon: 'tabler-circle-letter-s', url: 'https://...' }],
      opening_date: '2024-08-01',
      closing_date: '2024-09-01',
    }])

    const getJobList = async () => {
      try {
        const res = await jobApi.getJobList()

        console.log('getJobList: ', res)
        jobList.value = res.data
      }
      catch (error) {
        console.log('getJobList error: ', error)
      }
    }

    return {
      job,
      jobList,
      getJobList,

    }
  },
  {
    persist: true, // 지속성-persistence store이 되게 설정 (Composition API)
  },
)
