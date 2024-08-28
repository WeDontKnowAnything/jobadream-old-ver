import { defineStore } from 'pinia'
import { ref } from 'vue'
import * as corporationApi from '@/api/corporation'
import * as searchApi from '@/api/search'

export const useCompanyStore = defineStore(

  // 스토어 이름 정의
  'company',
  () => {
    // 객체, 함수 선언 스코프
    const companyList = ref([{ id: '', name: '', text: '', count: '' }])
    const company = ref({ id: '', name: '' })

    const getCompanyList = async () => {
      try {
        const res = await corporationApi.getCorporationList()

        console.log('getCompanyList: ', res)
        companyList.value = res.data
      }
      catch (error) {
        console.log('getCompanyList error: ', error)
      }
    }

    const getSearchCompany = async (keyword: string) => {
      try {
        const res = await searchApi.getCorpSearch(keyword)

        console.log('getCompanyList: ', res)
        companyList.value = res.data
      }
      catch (error) {
        console.log('getCompanyList error: ', error)
      }
    }

    const getCompany = async (id: any) => {
      try {
        const res = await corporationApi.getCorporation(id)

        console.log('getCompany: ', res)
        company.value = res.data
        console.log('company: ', company.value)
      }
      catch (error) {
        console.log('getCompany error: ', error)
      }
    }

    return {
      company,
      companyList,
      getCompany,
      getCompanyList,
      getSearchCompany,

      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true, // 지속성-persistence store이 되게 설정 (Composition API)
  },
)
