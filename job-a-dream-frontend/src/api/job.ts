import { http } from '@/api/http'

export function getJobList() {
  return http.get('/api/v1/jobs')
}

export function getJob(data: any) {
  return http.get('/api/v1/jobs', { params: data })
}
