<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { VDataTable } from 'vuetify/labs/VDataTable'
import { useBoardStore } from '@/stores/boardStore'

const boardStore = useBoardStore()
const { postList } = storeToRefs(boardStore)

const totalPost = computed(() => postList.value.length)

const widgetData = ref([
  { title: '작성된 게시글 수', value: totalPost, icon: 'tabler-clipboard-check' },
])

const searchQuery = ref('')

// Data table options
const itemsPerPage = ref(10)
const page = ref(1)
const sortBy = ref()
const orderBy = ref()

// Data table Headers
const headers = [
  { title: '번호', key: 'post_id' },
  { title: '제목', key: 'title' },
  { title: '날짜', key: 'posting_date' },
  { title: '조회수', key: 'view_count' },
]

// Update data table options
const updateOptions = (options: any) => {
  page.value = options.page
  sortBy.value = options.sortBy[0]?.key
  orderBy.value = options.sortBy[0]?.order
}

// 필터링된 postList
const filteredPosts = computed(() => {
  if (!searchQuery.value)
    return postList.value

  // 제목(title)에 searchQuery 값이 포함된 게시글만 필터링
  return postList.value.filter(post =>
    post.title.toLowerCase().includes(searchQuery.value.toLowerCase()),
  )
})

onMounted(() => {
  boardStore.getPostList()
})
</script>

<template>
  <div>
    <VCard class="mb-6">
      <!-- 👉 Widgets  -->
      <VCardText>
        <VRow>
          <template
            v-for="(data, id) in widgetData"
            :key="id"
          >
            <VCol
              cols="12"
              sm="6"
              md="3"
              class="px-6"
            >
              <div
                class="d-flex justify-space-between"
                :class="$vuetify.display.xs
                  ? 'product-widget'
                  : $vuetify.display.sm
                    ? id < 2 ? 'product-widget' : ''
                    : ''"
              >
                <div class="d-flex flex-column gap-y-1">
                  <h4 class="text-h4">
                    {{ data.value }}
                  </h4>

                  <h6 class="text-h6">
                    {{ data.title }}
                  </h6>
                </div>

                <VAvatar
                  variant="tonal"
                  rounded
                  size="38"
                >
                  <VIcon
                    :icon="data.icon"
                    size="28"
                  />
                </VAvatar>
              </div>
            </VCol>
          </template>
        </VRow>
      </VCardText>
    </VCard>

    <VCard>
      <!-- 👉 Filters -->
      <VCardText>
        <div class="d-flex justify-sm-space-between justify-start flex-wrap gap-4">
          <VTextField
            v-model="searchQuery"
            density="compact"
            placeholder="게시글 검색"
            style=" max-inline-size: 400px; min-inline-size: 400px;"
          />
          <div class="d-flex gap-x-4 align-center">
            <AppSelect
              v-model="itemsPerPage"
              style="min-inline-size: 6.25rem;"
              :items="[5, 10, 20, 50, 100]"
            />
            <RouterLink :to="{ name: 'posts-add' }">
              <VBtn
                color="primary"
                prepend-icon="tabler-plus"
              >
                게시글 추가
              </VBtn>
            </RouterLink>
          </div>
        </div>
      </VCardText>
      <VDivider />
      <!-- 👉 Order Table -->
      <VDataTable
        v-model:items-per-page="itemsPerPage"
        v-model:page="page"
        :headers="headers"
        :items="filteredPosts"
        :items-length="totalPost"
        show-select
        class="text-no-wrap fixed-width-table"
        @update:options="updateOptions"
      >
        <!-- Post ID -->
        <template #item.post_id="{ item }">
          {{ item.post_id }}
        </template>
        <!-- Title -->
        <template #item.title="{ item }">
          <RouterLink
            :to="{ name: 'posts-post-id', params: { id: item.post_id } }"
            class="font-weight-medium"
          >
            {{ item.title }}
          </RouterLink>
        </template>

        <!-- Date -->
        <template #item.posting_date="{ item }">
          {{ item.posting_date }}
        </template>
        <!-- Count -->
        <template #item.view_count="{ item }">
          {{ item.view_count }}
        </template>

        <!-- pagination -->
        <template #bottom>
          <VDivider />

          <div class="d-flex align-center justify-sm-space-between justify-center flex-wrap gap-3 pa-5 pt-3">
            <p class="text-sm text-disabled mb-0">
              {{ paginationMeta({ page, itemsPerPage }, totalPost) }}
            </p>

            <VPagination
              v-model="page"
              :length="Math.ceil(totalPost / itemsPerPage)"
              :total-visible="$vuetify.display.xs ? 1 : Math.min(Math.ceil(totalPost / itemsPerPage), 5)"
            >
              <template #prev="slotProps">
                <VBtn
                  variant="tonal"
                  color="default"
                  v-bind="slotProps"
                  :icon="false"
                >
                  이전
                </VBtn>
              </template>

              <template #next="slotProps">
                <VBtn
                  variant="tonal"
                  color="default"
                  v-bind="slotProps"
                  :icon="false"
                >
                  다음
                </VBtn>
              </template>
            </VPagination>
          </div>
        </template>
      </VDataTable>
    </VCard>
  </div>
</template>

<style lang="scss" scoped>
.customer-title:hover{
  color: rgba(var(--v-theme-primary)) !important;
}

.product-widget{
  border-block-end: 1px solid rgba(var(--v-theme-on-surface), var(--v-border-opacity));
  padding-block-end: 1rem;
}

.fixed-width-table {
  inline-size: 100%;
  table-layout: fixed; /* 열 간격 고정 */
}

.fixed-width-table th,
.fixed-width-table td {
  overflow: hidden;
  inline-size: 25%; /* 각 열에 고정된 비율로 너비를 지정 (예: 4개의 열이라면 각 열을 25%씩) */
  text-overflow: ellipsis; /* 내용이 넘치면 생략(...) */
  white-space: nowrap; /* 텍스트가 줄 바꿈되지 않도록 */
}
</style>
