import { http } from '@/api/http'

export function getJobList() {
  return http.get('/api/v1/job/all')
}

export function getJob(id: any) {
  return http.get('/api/v1/job', { params: { job_id: id } })
}
