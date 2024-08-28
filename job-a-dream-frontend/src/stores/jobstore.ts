import { defineStore } from 'pinia'
import { ref } from 'vue'
import * as jobApi from '@/api/job'
import * as searchApi from '@/api/search'

export const useJobStore = defineStore(

  // 스토어 이름 정의
  'job',
  () => {
    // 객체, 함수 선언 스코프
    const job = ref({
      corp_name: 'Toss',
      title: 'NLP Engineer, 생성형 AI',
      position: '기획',
      location: '서울',
      job_url: [{ platform_name: '사람인', icon: 'tabler-circle-letter-s', url: 'https://...' }, { platform_name: '사람인', icon: 'tabler-circle-letter-s', url: 'https://...' }, { platform_name: '사람인', icon: 'tabler-circle-letter-s', url: 'https://...' }],
      opening_date: '2024-08-01',
      closing_date: '2024-09-01',
    })

    const jobList = ref([{
      id: '12',
      corp_name: 'Toss',
      title: 'NLP Engineer, 생성형 AI',
      position: '기획',
      location: '서울',
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

    const getJob = async (id: any) => {
      try {
        const res = await jobApi.getJob(id)

        job.value = res.data
        res.data.job_url.forEach((url: any, index: number) => {
          if (url.platform_name === '사람인')
            job.value.job_url[index].icon = 'tabler-circle-letter-s'
        })
      }
      catch (error) {
        console.log('getJob error: ', error)
      }
    }

    const getSearchJob = async (location: string[], position: string[], keyword: string) => {
      try {
        const res = await searchApi.getJobSearch(location, position, keyword)

        console.log('getJobSearch: ', res)
        jobList.value = res.data
      }
      catch (error) {
        console.log('getJobSearch error: ', error)
      }
    }

    return {
      job,
      jobList,
      getJob,
      getJobList,
      getSearchJob,
    }
  },
  {
    persist: true, // 지속성-persistence store이 되게 설정 (Composition API)
  },
)
