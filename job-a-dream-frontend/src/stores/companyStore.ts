import { defineStore } from 'pinia'
import { ref } from 'vue'
import * as corporationApi from '@/api/job'

export const useCompanyStore = defineStore(

  // 스토어 이름 정의
  'company',
  () => {
    // 객체, 함수 선언 스코프
    const companyList = ref([{ id: '12', name: '샘송', text: '', count: '103' }])
    const company = ref({ id: '12', name: '샘송' })

    const getCompanyList = async () => {
      try {
        const res = await corporationApi.getJobList()

        console.log('getJobList: ', res)
        companyList.value = res.data
      }
      catch (error) {
        console.log('getJobList error: ', error)
      }
    }

    return {
      company,
      companyList,
      getCompanyList,

      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true, // 지속성-persistence store이 되게 설정 (Composition API)
  },
)
