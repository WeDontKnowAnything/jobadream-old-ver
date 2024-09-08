<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useCompanyStore } from '@/stores/companyStore'

const companyStore = useCompanyStore()
const { companyList } = storeToRefs(companyStore)

const totalCompanys = computed(() => companyList.value.length)

const search = ref('')

// Data table options
const itemsPerPage = ref(12)
const page = ref(1)

const paginatedData = computed(() => {
  const start = (page.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value

  return companyList.value.slice(start, end)
})

const onSearchCompany = () => {
  companyStore.getSearchCompany(search.value)
}

onMounted(() => {
  companyStore.getCompanyList()
})
</script>

<template>
  <div>
    <VCard class="mb-6">
      <!-- 👉 Widgets  -->
      <VCol
        cols="12"
        class="d-flex px-6 py-6 align-end"
      >
        <AppTextField
          v-model="search"
          label="기업 검색"
          prepend-inner-icon="tabler-search"
          placeholder="기업 이름"
          class="me-3"
        />
        <VBtn
          color="primary"
          @click="onSearchCompany"
        >
          검색
        </VBtn>
      </VCol>
    </VCard>
    <VRow>
      <VCol
        v-for="data in paginatedData"
        :key="data.id"
        cols="12"
        md="6"
        lg="4"
      >
        <VCard>
          <VCardItem>
            <VCardTitle class="text-white">
              <RouterLink
                :to="{ name: 'company-id', params: { id: data.id } }"
                class="font-weight-medium"
              >
                {{ data.name }}
              </RouterLink>
            </VCardTitle>
          </VCardItem>

          <VCardText>
            <p class="clamp-text text-white mb-0">
              기업 요약 정보{{ data.text }}
            </p>
          </VCardText>

          <VCardText class="d-flex justify-space-between align-center flex-wrap">
            <div class="d-flex align-center">
              <IconBtn
                icon="tabler-eye-check"
                color="white"
                class="me-1"
              />
              <span class="text-subtitle-2 text-white mt-1"> 조회수 {{ data.count }}</span>
            </div>
          </VCardText>
        </VCard>
      </VCol>
    </VRow>

    <div class="d-flex align-center justify-sm-space-between justify-center flex-wrap gap-3 pa-5 pt-3">
      <p class="text-sm text-disabled mb-0">
        {{ paginationMeta({ page, itemsPerPage }, totalCompanys) }}
      </p>

      <VPagination
        v-model="page"
        :length="Math.ceil(totalCompanys / itemsPerPage)"
        :total-visible="$vuetify.display.xs ? 1 : Math.min(Math.ceil(totalCompanys / itemsPerPage), 5)"
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
</style>
