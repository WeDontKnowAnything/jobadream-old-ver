<script lang="ts" setup>
import { storeToRefs } from 'pinia'
import { useBoardStore } from '@/stores/boardStore'

const boardStore = useBoardStore()
const { comments, newComment, post } = storeToRefs(boardStore)

const router = useRouter()
const route = useRoute()
const commentRules = [(v: string) => v.length <= 250 || '최대 250자까지 작성 가능']

const saveComment = () => {
  console.log(newComment.value)
}

const resetComment = () => {
  newComment.value.content = ''
}

const backToBoard = () => {
  router.go(-1)
}

onMounted(() => {
  if ('id' in route.params)
    newComment.value.post_id = route.params.id as string
  else
    console.error('Route parameter id is missing')
})
</script>

<template>
  <VRow>
    <VCol
      cols="12"
      md="7"
    >
      <VCard>
        <VCardText class=" text-end">
          <span>
            게시일 : {{ post.posting_date }}
          </span>
        </VCardText>
        <VCardText>
          <AppTextField
            v-model="post.title"
            label="제목"
            readonly
          />
        </VCardText>
        <VCardText>
          <AppTextarea
            v-model="post.content"
            label="내용"
            readonly
          />
        </VCardText>
      </VCard>

      <VBtn
        prepend-icon="tabler-arrow-left"
        block
        class="mt-4"
        color="warning"
        @click="backToBoard"
      >
        이전
      </VBtn>
    </VCol>
    <VCol
      cols="12"
      md="5"
    >
      <VCard title="댓글 목록">
        <VCardText>
          <AppTextarea
            v-model="newComment"
            prepend-inner-icon="tabler-message-2"
            rows="2"
            :rules="commentRules"
            label="댓글 추가"
            placeholder="댓글을 '잡어드림'"
          />
        </VCardText>
        <VCardText>
          <VRow>
            <VCol cols="6">
              <!-- 👉 Send Invoice -->
              <VBtn
                block
                prepend-icon="tabler-message-2"
                @click="saveComment"
              >
                댓글
              </VBtn>
            </VCol>
            <VCol cols="6">
              <!-- 👉 Preview -->
              <VBtn
                block
                color="default"
                variant="tonal"
                @click="resetComment"
              >
                취소
              </VBtn>
            </VCol>
          </VRow>
        </VCardText>
        <VDivider />
        <template
          v-for="comment in comments"
          :key="comment"
        >
          <VCardText>
            <VTimeline
              side="end"
              align="start"
              line-inset="8"
              truncate-line="both"
              density="compact"
            >
              <!-- SECTION Timeline Item: Flight -->
              <VTimelineItem
                dot-color="blue"
                size="x-small"
              >
                <div class="d-flex justify-space-between align-center flex-wrap mb-1">
                  <div class="app-timeline-title">
                    {{ boardStore.getRandomName() }}
                  </div>
                  <span class="app-timeline-meta">{{ comment.comment_date }}</span>
                </div>

                <div class="app-timeline-text">
                  {{ comment.content }}
                </div>
              </VTimelineItem>
              <!-- !SECTION -->
            </VTimeline>
          </VCardText>
        </template>
      </VCard>
    </VCol>
  </VRow>
</template>
