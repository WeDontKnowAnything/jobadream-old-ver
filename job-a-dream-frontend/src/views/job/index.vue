<script lang="ts" setup>
const postTitle = ref('')
const postText = ref('')
const newComment = ref('')

const comments = ref([
  { content: '마 볶아 온나', comment_date: '2021-21-23 10:11' },
  { content: '마 볶아 온나', comment_date: '2021-21-23 10:11' },
  { content: '마 볶아 온나', comment_date: '2021-21-23 10:11' },
])

const commentRules = [(v: string) => v.length <= 250 || '최대 250자까지 작성 가능']

const randomName = ref(['꿈이 있는 청년', '희망을 품고 있는 청년', '가능성이 보이는 청년', '보기 드문 청년', '제육볶음 잘 볶을 것 같은 청년', '정직한 청년'])

// 랜덤하게 이름을 뽑아주는 함수
const getRandomName = () => {
  const randomIndex = Math.floor(Math.random() * randomName.value.length)

  return randomName.value[randomIndex]
}
</script>

<template>
  <VRow>
    <VCol
      cols="12"
      md="7"
    >
      <VCard>
        <VCardText>
          <AppTextField
            v-model="postTitle"
            label="제목"
          />
        </VCardText>
        <VCardText>
          <AppTextarea
            v-model="postText"
            label="내용"
            placeholder="내용을 '잡어드림'"
            auto-grow
          />
        </VCardText>
      </VCard>
    </VCol>
    <!-- 👉 Radar Chart -->
    <VCol
      cols="12"
      md="5"
    >
      <VCard class="mb-6">
        <VDivider />
        <VCardText>
          <VRow>
            <VCol cols="6">
              <!-- 👉 Send Invoice -->
              <VBtn
                block
                prepend-icon="tabler-send"
              >
                게시글 저장
              </VBtn>
            </VCol>

            <VCol cols="6">
              <!-- 👉 Preview -->
              <VBtn
                block
                color="default"
                variant="tonal"
              >
                취소
              </VBtn>
            </VCol>
          </VRow>
        </VCardtext>
      </VCard>
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
              >
                취소
              </VBtn>
            </VCol>
          </VRow>
        </VCardText>
        <VDivider />
        <template
          v-for="(comment, index) in comments"
          :key="index"
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
                    {{ getRandomName() }}
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
      </vcard>
    </VCol>
  </VRow>
</template>
