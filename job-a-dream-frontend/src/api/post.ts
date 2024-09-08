import { http } from '@/api/http'

export function getPostList() {
  return http.get('/api/v1/post/all')
}

export function getPost(id: any) {
  return http.get('/api/v1/post', { params: { post_id: id } })
}

export function addPost(data: any) {
  return http.post('/api/v1/post', data)
}

export function getComments(id: any) {
  return http.get('/api/v1/post/comments', { params: { post_id: id } })
}

export function addComment(data: any) {
  return http.post('/api/v1/post/comments', data)
}
