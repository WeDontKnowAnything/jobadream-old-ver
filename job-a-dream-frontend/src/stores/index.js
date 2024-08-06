import { defineStore } from 'pinia'
import { ref } from 'vue'

export const storeName = defineStore(
  // 스토어 이름 정의
  'yourStore',
  () => {
    // 객체, 함수 선언 스코프
    const honey = ref('')
    return {
      honey
      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true // 지속성-persistence store이 되게 설정 (Composition API)
  }
)
