<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useCompanyStore } from '@/stores/companyStore'

const companyStore = useCompanyStore()
const { company } = storeToRefs(companyStore)
const route = useRoute()
const currentTab = ref(0)

onMounted(() => {
  if ('id' in route.params) {
    const id = route.params.id

    companyStore.getCompany(id)
  }
})
</script>

<template>
  <VRow>
    <!-- 👉 Radar Chart -->
    <VCol cols="12">
      <VCard :title="company.name">
        <VCardText>
          {{ company.name }}
        </VCardText>
      </VCard>
    </VCol>
    <VCol cols="12">
      <VCard>
        <VTabs v-model="currentTab">
          <VTab>정보</VTab>
          <VTab>기업 전체 채용 공고 목록</VTab>
        </VTabs>

        <VCardText>
          <VWindow v-model="currentTab">
            <VWindowItem>
              <VCardText>
                {{ company.name }}
              </VCardText>
            </VWindowItem>
            <VWindowItem>
              <VCardText>
                <template v-if="!company.jobs || company.jobs.length === 0">
                  해당 기업에서 진행하는 채용 공고가 없습니다.
                </template>
                <VExpansionPanels
                  multiple
                  class="no-icon-rotate"
                >
                  <VExpansionPanel
                    v-for="job in company.jobs"
                    :key="job.title"
                  >
                    <VExpansionPanelTitle disable-icon-rotate>
                      {{ job.title }}
                      <template #actions>
                        <VChip
                          color="info"
                          label
                        >
                          {{ job.position }}
                        </VChip>
                      </template>
                    </VExpansionPanelTitle>
                    <VExpansionPanelText>
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
                    </VExpansionPanelText>
                  </VExpansionPanel>
                </VExpansionPanels>
              </VCardText>
            </VWindowItem>
          </VWindow>
        </VCardText>
      </VCard>
    </VCol>
  </VRow>
</template>
