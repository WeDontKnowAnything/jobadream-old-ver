<script lang="ts" setup>
import { storeToRefs } from 'pinia'
import { useBoardStore } from '@/stores/boardStore'

const boardStore = useBoardStore()
const { newPost } = storeToRefs(boardStore)
const router = useRouter()

const savePost = () => {
  boardStore.addPost()
  router.go(-1)
}

const resetPost = () => {
  router.go(-1)
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
            v-model="newPost.title"
            label="제목"
          />
        </VCardText>
        <VCardText>
          <AppTextarea
            v-model="newPost.content"
            label="내용"
            placeholder="내용을 '잡어드림'"
            auto-grow
          />
        </VCardText>
      </VCard>
    </VCol>
    <VCol
      cols="12"
      md="5"
    >
      <VCard class="mb-6">
        <VDivider />
        <VCardText>
          <VRow>
            <VCol cols="6">
              <!-- 👉 게시글 저장 -->
              <VBtn
                block
                prepend-icon="tabler-send"
                @click="savePost"
              >
                게시글 저장
              </VBtn>
            </VCol>

            <VCol cols="6">
              <!-- 👉 초기화 -->
              <VBtn
                block
                color="default"
                variant="tonal"
                @click="resetPost"
              >
                취소
              </VBtn>
            </VCol>
          </VRow>
        </VCardtext>
      </VCard>
    </VCol>
  </VRow>
</template>
