import qs from 'qs'
import { http } from '@/api/http'

export function getCorpSearch(keyword: string) {
  return http.get(`/api/v1/search/corporations?keyword=${keyword}`)
}

export function getJobSearch(location: string[], position: string[], keyword: string) {
  return http.get('/api/v1/search/jobs', {
    params: { location, position, keyword },

    // 배열 파라미터가 location[]=가 아닌 location=으로 전송되도록 설정
    paramsSerializer: params => {
      return qs.stringify(params, { arrayFormat: 'repeat' })
    },
  })
}

export function getPostSearch(keyword: string) {
  return http.get(`/api/v1/search/posts?keywords=${keyword}`)
}
