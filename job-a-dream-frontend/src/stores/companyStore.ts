import { defineStore } from 'pinia'
import { ref } from 'vue'
import * as corporationApi from '@/api/corporation'
import * as searchApi from '@/api/search'

export const useCompanyStore = defineStore(

  // 스토어 이름 정의
  'company',
  () => {
    // 객체, 함수 선언 스코프
    const companyList = ref([{ id: '1', name: '2', text: '2', count: '1' }])

    const company = ref({
      id: '00266961',
      name: 'NAVER',
      jobs: [
        {
          corp_name: 'NAVER',
          title: '[네이버웹툰] [경력] Data Scientist (추천시스템 ML모델링)',
          position: 'IT개발·데이터',
          job_url: [
            {
              platform_name: '사람인',
              icon: 'tabler-circle-letter-s',
              url: 'https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=48846279&recommend_ids=eJxVj7kVA1EIA6txzvUlEW8h238XazswOJw3SEBJpClvOV%2B8SowD%2Bt3mX0SrLcZ6ldsPYWbwsXIjB3HYg%2BpA1cqGDGMDAU22Mq3%2BMM4Mw6Ee2ydyLSLhc5UqkWsRmDnNyvCD9b48VlXwHfjgA7VGQOk%3D&view_type=search&searchword=%EB%84%A4%EC%9D%B4%EB%B2%84&searchType=search&gz=1&t_ref_content=generic&t_ref=search&relayNonce=dba41cb387a6705b5a35&paid_fl=n&search_uuid=1e9e540d-c486-4615-9945-6786d08f71bb&immediately_apply_layer_open=n',
            },
          ],
        },
      ],
    })

    const getCompanyList = async () => {
      try {
        const res = await corporationApi.getCorporationList()

        companyList.value = res.data
      }
      catch (error) {
        console.log('getCompanyList error: ', error)
      }
    }

    const getSearchCompany = async (keyword: string) => {
      try {
        const res = await searchApi.getCorpSearch(keyword)

        companyList.value = res.data
      }
      catch (error) {
        console.log('getCompanyList error: ', error)
      }
    }

    const setPlatformIcon = (platformName: string) => {
      if (platformName === '사람인')
        return 'tabler-circle-letter-s'

      // 다른 플랫폼에 대한 아이콘 로직을 추가할 수 있음
      return 'default-icon'
    }

    const getCompany = async (id: any) => {
      try {
        const res = await corporationApi.getCorporation(id)

        // 새롭게 jobs 데이터를 생성하면서 icon을 설정
        const updatedJobs = res.data.jobs.map((job: any) => {
          const updatedJobUrl = job.job_url.map((url: any) => ({
            ...url,
            icon: setPlatformIcon(url.platform_name), // 플랫폼 이름에 따라 아이콘 설정
          }))

          return {
            ...job,
            job_url: updatedJobUrl, // 변환된 job_url 배열을 포함
          }
        })

        // 새로운 jobs 배열을 company에 반영
        company.value = {
          ...res.data,
          jobs: updatedJobs, // 업데이트된 jobs 배열
        }
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
)
