import { http } from '@/api/http'

export function getCorporationList() {
  return http.get('/api/v1/corporations')
}

export function getCorporation(id: any) {
  return http.get('/api/v1/corporations', { params: id })
}

export function getCorporationJob(id: any) {
  return http.get('/api/v1/corporations/jobs', { params: id })
}
