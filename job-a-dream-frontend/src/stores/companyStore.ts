import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useCompanyStore = defineStore(

  // 스토어 이름 정의
  'company',
  () => {
    // 객체, 함수 선언 스코프
    const company = ref({ corp_name: '샘송' })

    return {
      company,

      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true, // 지속성-persistence store이 되게 설정 (Composition API)
  },
)
