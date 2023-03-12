<template>
  <div class="body" @click="$store.commit('changeVoteUserRecord')">
    <div
      class="body_table"
      @click="
        (e) => {
          e.stopPropagation();
        }
      "
    >
      <el-table
        class="body_el_table"
        v-if="tableData"
        :data="tableData"
        stripe
        style="width: 100%"
      >
        <el-table-column prop="userId" label="选手编号" width="180"
          ><template #default="scope">
            <el-button link type="primary" size="small">{{
              "#" + scope.row.userId
            }}</el-button></template
          ></el-table-column
        >
        <el-table-column prop="count" label="票数" width="180">
          <template #default="scope">
            <div v-if="!scope.row.isEdit">{{ scope.row.count }}</div>
            <el-input v-else type="text" v-model="scope.row.count"
          /></template>
        </el-table-column>
        <el-table-column prop="detail" label="详情" width="180">
          <template #default="scope">
            <div
              v-if="!scope.row.isEdit"
              style="
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
              "
            >
              {{ scope.row.detail }}
            </div>
            <el-input
              v-else
              v-model="scope.row.detail"
              :rows="5"
              type="textarea"
          /></template>
        </el-table-column>
        <el-table-column prop="name" label="选手名称" width="180">
          <template #default="scope">
            <div v-if="!scope.row.isEdit">{{ scope.row.name }}</div>
            <el-input v-else type="text" v-model="scope.row.name"
          /></template>
        </el-table-column>
        <el-table-column prop="status" label="审核状态" width="180">
          <template #default="scope">
            <el-switch
              @change="changeStatus(scope.row.userId)"
              :model-value="scope.row.status === 1 ? true : false"
          /></template>
        </el-table-column>
        <el-table-column prop="avator" label="选手头像" width="180">
          <template #default="scope">
            <img
              :src="HOST + '/media/' + scope.row.avator"
              width="30"
              height="30"
              alt=""
            />
          </template>
        </el-table-column>
        <el-table-column label="操作" width="180">
          <template #default="scope">
            <span
              v-if="!scope.row.isEdit"
              style="margin-right: 20px; color: #2479fb; cursor: pointer"
              @click="editVoteUser(scope.row.userId)"
              >编辑</span
            >
            <span
              v-else
              style="margin-right: 20px; color: #2479fb; cursor: pointer"
              @click="saveEidt({ ...scope.row })"
              >保存</span
            >
          </template>
        </el-table-column>
      </el-table>
      <div class="export" @click="exportData">
        <svg
          t="1678536331275"
          class="icon"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="2592"
          width="30"
          height="30"
        >
          <path
            d="M1024 748.544q0 25.6-8.704 48.128t-24.064 40.96-36.352 30.208-45.568 15.872l0 2.048-21.504 0-1.024 0-664.576 0q-2.048 0-2.56 0.512t-2.56 0.512-3.072-0.512-3.072-0.512l-6.144 0 0-1.024q-43.008-2.048-80.384-19.456t-65.024-46.592-43.52-67.584-15.872-81.408 15.872-80.896 43.008-66.56 63.488-47.104 78.336-21.504q7.168-66.56 36.864-124.416t76.288-100.864 107.008-67.584 129.024-24.576q72.704 0 137.216 27.648t112.128 75.776 75.264 112.128 27.648 136.704q0 32.768-6.144 64t-17.408 59.904q2.048 0 4.608-0.512t4.608-0.512q28.672 0 53.248 10.752t43.008 29.184 29.184 43.52 10.752 53.76zM687.104 596.992q12.288-20.48 7.168-23.552t-25.6-3.072q-12.288 0-34.304-0.512t-33.28-0.512q-16.384 0-20.992-13.312t-4.608-36.864q0-32.768-0.512-52.736t-0.512-43.52q0-26.624-3.584-38.912t-29.184-12.288q-18.432 0-27.648 0.512t-25.6 0.512q-27.648 0-34.304 15.872t-6.656 31.232l0 32.768q0 13.312 0.512 25.6t0.512 25.6l0 29.696q0 16.384-4.096 25.088t-19.456 8.704q-6.144 1.024-16.896 1.536t-22.016 1.024-21.504 0.512l-16.384 0q-21.504 0-25.6 13.312t13.312 33.792q17.408 21.504 37.376 46.592t39.424 50.688 37.376 49.664 33.28 41.472q27.648 30.72 53.248-1.024 15.36-17.408 35.84-45.056t41.984-57.856 40.96-58.368 31.744-46.592z"
            p-id="2593"
            fill="#3bc214"
          ></path>
        </svg>
      </div>
      <div class="export" style="top: 40px">
        <svg
          @click="changeIsUpload"
          t="1678536258124"
          class="icon"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="1518"
          width="30"
          height="30"
        >
          <path
            d="M1024 693.248q0 25.6-8.704 48.128t-24.576 40.448-36.864 30.208-45.568 16.384l1.024 1.024-17.408 0-4.096 0-4.096 0-675.84 0q-5.12 1.024-16.384 1.024-39.936 0-74.752-15.36t-60.928-41.472-40.96-60.928-14.848-74.752 14.848-74.752 40.96-60.928 60.928-41.472 74.752-15.36l1.024 0q-1.024-8.192-1.024-15.36l0-16.384q0-72.704 27.648-137.216t75.776-112.128 112.128-75.264 136.704-27.648 137.216 27.648 112.64 75.264 75.776 112.128 27.648 137.216q0 37.888-8.192 74.24t-22.528 69.12q5.12-1.024 10.752-1.536t10.752-0.512q27.648 0 52.736 10.752t43.52 29.696 29.184 44.032 10.752 53.76zM665.6 571.392q20.48 0 26.624-4.608t-8.192-22.016q-14.336-18.432-31.744-48.128t-36.352-60.416-38.4-57.344-37.888-38.912q-18.432-13.312-27.136-14.336t-25.088 12.288q-18.432 15.36-35.84 38.912t-35.328 50.176-35.84 52.224-36.352 45.056q-18.432 18.432-13.312 32.768t25.6 14.336l16.384 0q9.216 0 19.968 0.512t20.992 0.512l17.408 0q14.336 1.024 18.432 9.728t4.096 24.064q0 17.408-0.512 30.72t-0.512 25.6-0.512 25.6-0.512 30.72q0 7.168 1.536 15.36t5.632 15.36 12.288 11.776 21.504 4.608l23.552 0q9.216 0 27.648 1.024 24.576 0 28.16-12.288t3.584-38.912q0-23.552 0.512-42.496t0.512-51.712q0-23.552 4.608-36.352t19.968-12.8q11.264 0 32.256-0.512t32.256-0.512z"
            p-id="1519"
            fill="#d81e06"
          ></path>
        </svg>
      </div>
      <div class="upload_area" v-show="isShowUpload">
        <input
          type="file"
          id="upload"
          @change="patchUploadTarget"
          style="display: none"
        />
        <div class="upload" @click="dispatchClick">+</div>
        <a
          class="download"
          href="http://123.60.38.9:8000/media/template/批量上传模板.xlsx"
          download="批量上传模板"
          >下载模板文件</a
        >
      </div>
    </div>
  </div>
</template>

<script setup>
import { useStore } from "vuex";
import { fether } from "@/utils/fether";
import { reactive, ref } from "vue";
import { HOST } from "@/ENV";
import jsCookie from "js-cookie";
import XLSX from "xlsx";
import { useRouter } from "vue-router";
const $store = new useStore();
const tableData = reactive([]);
const $router = useRouter();

const isShowUpload = ref(false);

// 请求投票选手列表
const getUserVoteData = async () => {
  let result = await fether(
    `/votetarget/?vote_id=${$store.state.voteManagerUserRecordVoteid}`
  );
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data);
    JSONResult.forEach((item) => {
      tableData.push({
        avator: item.fields.avator,
        count: item.fields.count,
        detail: item.fields.detail,
        name: item.fields.name,
        vote_id: item.fields.vote_id,
        isEdit: false,
        userId: item.pk,
        status: item.fields.status,
      });
    });
  } else {
    // 请求发送错误
    await $store.dispatch("GlobalMessageActions", "操作失败,请重试");
  }
};
getUserVoteData();

// 使可编辑
const editVoteUser = (pk) => {
  tableData.forEach((item, index) => {
    if (item.userId === pk) {
      tableData[index].isEdit = true;
    } else {
      tableData[index].isEdit = false;
    }
  });
};
// 提交编辑
const saveEidt = async (target) => {
  let result = await fether(`/votetarget/`, "put", {
    ...target,
    token: jsCookie.get("token"),
  });
  if (result.code === 200) {
    tableData.forEach((item, index) => {
      tableData[index].isEdit = false;
    });
  }
  await $store.dispatch("GlobalMessageActions", result.msg);
};

// 导出execl
const exportData = () => {
  const excleData = [
    ["选手编号", "票数", "选手介绍", "姓名", "所属活动ID", "审核状态"],
  ];
  tableData.forEach((item) => {
    excleData.push([
      item.userId,
      item.count,
      item.detail,
      item.name,
      item.vote_id,
      item.status === 1 ? "通过" : "未通过",
    ]);
  });
  const options = {
    "!cols": [
      { wpx: 100 },
      { wpx: 100 },
      { wpx: 100 },
      { wpx: 100 },
      { wpx: 100 },
      { wpx: 100 },
      { wpx: 100 },
    ],
  };
  // json方式导入数据
  const worksheet = XLSX.utils.json_to_sheet(excleData);

  worksheet["!cols"] = options["!cols"]; // 设置每列的列宽，10代表10个字符，注意中文占2个字符
  // worksheet["!merges"] = [{ e: { c: 1, r: 1 }, s: { c: 0, r: 0 } }]; //合并单元格
  // 新建一个工作簿
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, "Sheet1");
  XLSX.writeFile(workbook, `活动选手汇总表.xlsx`);
};

// 批量上传选手
const patchUploadTarget = () => {
  let box = document.getElementById("upload").files[0];
  let form = new FormData();
  form.append("file", box);
  form.append("token", jsCookie.get("token"));
  fetch(`${HOST}/addvotetargets/`, {
    method: "post",
    body: form,
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.code === 200) {
        $store.dispatch("GlobalMessageActions", "任务已成功添加,请等待");
        $store.commit("changeVoteManageUser");
        $store.dispatch("SubNavBarActions", {
          item: [
            {
              name: "执行中",
              description: "显示执行中的任务",
              path: "/progresstask",
            },
          ],
          navName: "执行中",
        });
        $router.push("/progresstask");
      } else {
        $store.dispatch("GlobalMessageActions", data.msg);
      }
    });
};

const changeIsUpload = () => {
  isShowUpload.value = !isShowUpload.value;
};

// 更改状态
const changeStatus = async (pk) => {
  for (let i = 0; i < tableData.length; i++) {
    if (tableData[i].userId === pk) {
      tableData[i].status = tableData[i].status === 1 ? 0 : 1;
      let result = await fether("/updatetargetstatus/", "put", {
        token: jsCookie.get("token"),
        data: { pk: pk, status: tableData[i].status },
      });
      await $store.dispatch("GlobalMessageActions", result.msg);
      break;
    }
  }
};

// 分发clilk事件
const dispatchClick = () => {
  let box = document.getElementById("upload");
  box.click();
};
</script>

<style lang="scss" scoped>
.body {
  position: absolute;
  bottom: 0px;
  left: 0;
  right: 0;
  top: 0;
  background-color: #00000074;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 5;
}
.body_table {
  width: 50%;
  height: 80%;
  background-color: white;
  border-radius: 5px;
  padding: 10px;
  position: relative;
}

.body_el_table {
  height: 100%;
}
.export {
  position: absolute;
  top: 0px;
  right: -50px;
  cursor: pointer;
}
.upload_area {
  position: absolute;
  top: 40px;
  right: -200px;
  background-color: white;
  border-radius: 3px;
  padding: 10px;
  div {
    margin: 5px;
    font-style: italic;
  }
}
.download {
  color: #0d6efd;
  font-size: 10px;
  text-align: end;
}
.download:hover {
  color: #a5a5a5;
  text-decoration: underline;
  cursor: pointer;
}
.upload {
  height: 100px;
  width: 100px;
  border: 2px dashed #cecece;
  border-radius: 3px;
  font-size: 30px;
  color: #cecece;
  cursor: pointer;
  line-height: 100px;
  text-align: center;
  font-style: normal;
}
</style>
