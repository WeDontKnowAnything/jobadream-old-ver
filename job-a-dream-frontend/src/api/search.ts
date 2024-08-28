import { http } from '@/api/http'

export function getCorpSearch(keyword: string) {
  return http.get(`/api/v1/search/corporation/?keywords=${keyword}`)
}

export function getJobSearch(location: string[], position: string[], keyword: string) {
  return http.get(`/api/v1/search/jobs?location=${location}&position=${position}&keyword=${keyword}`)
}

export function getPostSearch(keyword: string) {
  return http.get(`/api/v1/search/posts/?keywords=${keyword}`)
}
