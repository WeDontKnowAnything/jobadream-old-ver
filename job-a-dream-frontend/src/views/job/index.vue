<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useJobStore } from '@/stores/jobStore'

const jobStore = useJobStore()
const { job } = storeToRefs(jobStore)

// const job = ref({
//   corp_name: 'Toss',
//   title: 'NLP Engineer, 생성형 AI',
//   category_code: '13',
//   location: '서울',
//   experience_type: '신입',
//   job_url: [{ saramin: 'https://...' }, { jobkorea: 'https://...' }],
//   opening_date: '2024-08-01',
//   closing_date: '2024-09-01',
// })
const currentTab = ref(0)
</script>

<template>
  <VRow class="py-6">
    <!-- 👉 Welcome -->
    <VCol
      cols="12"
      md="8"
      :class="$vuetify.display.mdAndUp ? 'border-e' : 'border-b'"
    >
      <div class="pe-3">
        <div
          class="mb-2 text-wrap"
          style="max-inline-size: 400px;"
        >
          {{ job.corp_name }}
        </div>
        <h3 class="text-h3 text-high-emphasis mb-4">
          {{ job.title }}
        </h3>
        <div class="d-flex gap-2">
          <VChip
            color="success"
            label
          >
            {{ job.location }}
          </VChip>
          <VChip
            color="info"
            label
          >
            {{ job.experience_type }}
          </VChip>
        </div>
      </div>
    </VCol>
    <!-- 👉 Time Spendings -->
    <VCol
      cols="12"
      md="4"
    >
      <div class="d-flex justify-space-between align-center">
        <div class="d-flex flex-column ps-3">
          <h5 class="text-h5 text-high-emphasis mb-4 text-no-wrap">
            일정
          </h5>
          <div class="d-flex mb-3 align-center">
            <VChip
              variant="outlined"
              color="success"
              class="me-2"
            >
              시작일
            </VChip>
            <span class="">
              {{ job.opening_date }}
            </span>
          </div>
          <div class="d-flex align-center">
            <VChip
              variant="outlined"
              color="error"
              class="me-2"
            >
              종료일
            </VChip>
            <span>
              {{ job.closing_date }}
            </span>
          </div>
        </div>
      </div>
    </VCol>
  </VRow>
  <VCard>
    <VTabs v-model="currentTab">
      <VTab>정보</VTab>
      <VTab>채용 공고</VTab>
    </VTabs>

    <VCardText>
      <VWindow v-model="currentTab">
        <VWindowItem>
          <VCardText>
            {{ job.corp_name }}
          </VCardText>
        </VWindowItem>
        <VWindowItem>
          <VCardText>
            <VList class="card-list">
              <VRow
                no-gutters
                class="d-flex"
              >
                <VCol
                  v-for="(job_url, idx) in job.job_url"
                  :key="idx"
                  cols="12"
                  md="6"
                >
                  <VListItem class="mb-4">
                    <template #prepend>
                      <VAvatar
                        color="info"
                        variant="tonal"
                        size="34"
                        rounded
                      >
                        <VIcon :icon="job_url.icon" />
                      </VAvatar>
                    </template>
                    <VListItemTitle class="font-weight-medium">
                      {{ job_url.platform_name }}
                    </VListItemTitle>

                    <template #append>
                      <a
                        :href="job_url.url"
                        class="text-decoration-none"
                      >
                        <span class="font-weight-medium me-4">링크로 바로 이동</span>
                      </a>
                    </template>
                  </VListItem>
                </VCol>
              </VRow>
            </VList>
          </VCardText>
        </VWindowItem>
      </VWindow>
    </VCardText>
  </VCard>
</template>
