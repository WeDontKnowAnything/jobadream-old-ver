import { http } from '@/api/http'

export function getCorpSearch(keyword: string) {
  return http.get(`/api/v1/search/corporation/?keywords=${keyword}`)
}

export function getJobSearch(formData: any) {
  return http.get('/api/v1/search/job/', { params: formData })
}

export function getPostSearch(keyword: string) {
  return http.get(`/api/v1/search/posts/?keywords=${keyword}`)
}
