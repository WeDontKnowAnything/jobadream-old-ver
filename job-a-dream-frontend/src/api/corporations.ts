import { http } from '@/api/http'

export function getCorporationsList() {
  return http.get('/api/v1/corporations')
}

export function getCorporation(data: any) {
  return http.get('/api/v1/corporations', { params: data })
}

export function getCorporationJob(data: any) {
  return http.get('/api/v1/corporations/jobs', { params: data })
}
