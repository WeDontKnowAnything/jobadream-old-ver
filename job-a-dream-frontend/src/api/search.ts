import { http } from '@/api/http'

export function getCorpSearch(keyword: string) {
  return http.get(`/api/v1/search/corporations?keyword=${keyword}`)
}

export function getJobSearch(location: string[], position: string[], keyword: string) {
  return http.get('/api/v1/search/jobs', { params: { location, position, keyword } })
}

export function getPostSearch(keyword: string) {
  return http.get(`/api/v1/search/posts?keywords=${keyword}`)
}
