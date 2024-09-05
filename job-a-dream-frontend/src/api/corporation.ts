import { http } from '@/api/http'

export function getCorporationList() {
  return http.get('/api/v1/corporation/all')
}

export function getCorporation(id: any) {
  return http.get('/api/v1/corporation', { params: { corp_id: id } })
}

export function getCorporationJob(id: any) {
  return http.get('/api/v1/corporations/jobs', { params: { corp_id: id } })
}
