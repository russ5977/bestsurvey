<template>
  <div>
    <div class="top_title" style="height: 60px">
      <div class="col-xs-5 col-sm-4 path-img jiayin">
        <img style="width: 100%" src="../utils//img//1.png" />
      </div>

      <div class="questionnaire_list">
        <a href="/main_page">
          <el-button type="primary" plain>问卷列表</el-button></a
        >
      </div>

      <div class="personal_data">
        <a href="/personal_data"
          ><el-button type="primary" plain>个人数据</el-button></a
        >
      </div>

      <div class="platform_statistics">
        <a><el-button type="primary" plain>平台统计</el-button></a>
      </div>
      <div class="search_class">
        <div class="num">编号</div>
        <div class="num1">
          <el-input v-model="keyword" placeholder="项目编号"></el-input>
        </div>
        <div class="status">状态</div>
        <div class="status1">
          <el-input v-model="keyword" placeholder="已成功/未通过/已退款"></el-input>
        </div>
        <div class="plat">平台</div>
        <div class="plat1" style="margin-left: 15%">
          <el-input v-model="keyword" placeholder="A/B/C/D"></el-input>
        </div>
        <div class="time">时间</div>
        <div class="block time1">
          <el-date-picker
            v-model="value2"
            type="daterange"
            align="right"
            unlink-panels
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            :picker-options="pickerOptions"
          >
          </el-date-picker>
        </div>
        <div class="search_button1">
          <el-button type="primary" round @click="search_survey"
            >搜索</el-button
          >
        </div>
      </div>
    </div>
  </div>
  <a href="/self_message"
    ><div class="setting"><b class="el-icon-setting"></b></div
  ></a>
  <div class="full">
    <b class="el-icon-message"></b>
  </div>
    <div class="person_main">
      <el-table :data="houselist" border stripe>
        <el-table-column label="编号" prop="number"></el-table-column>
        <el-table-column label="项目" prop="introduction"></el-table-column>
        <el-table-column label="价格" prop="price"></el-table-column>
        <el-table-column label="平台" prop="platfrom"></el-table-column>
        <el-table-column label="状态" prop="status"></el-table-column>
        <el-table-column label="开始时间" prop="starttime"></el-table-column>
        <el-table-column label="结束时间" prop="endtime"></el-table-column>
        <el-table-column label="IP" prop="ip"></el-table-column>
        <el-table-column label="耗时(分钟)" prop="time"></el-table-column>
        <el-table-column label="操作">
          <div class="join">
            <el-button type="primary" round>备注</el-button>
          </div>
          <br />
        </el-table-column> </el-table
      ><br /><br />
      <el-pagination
        :current-page="queryInfo.pagenum"
        :page-sizes="[5, 10, 20, 30, 50]"
        :page-size="queryInfo.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      >
      </el-pagination>
    </div>
</template>
    
    <script>
import Axios from "axios";
export default {
  data() {
    return {
      queryInfo: {
        query: "", // 查询参数
        pagenum: 1, // 当前页码
        page: 1,
        pagesize: 5, // 每页显示条数
      },
      total: 0,
      houselist: [],
      username: localStorage.getItem("username"),
      keyword: "",
      pickerOptions: {},
    };
  },
  methods: {
    search_survey() {
      Axios.post("/main/search/", { keyword: this.keyword })
        .then((resp) => {
          console.log(resp.data);
          this.houselist = resp.data.data;
          console.log(">>>>>>>>>>>>this.list1", this.houselist);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
    
    <style>
.top_title {
  width: 100%;
  background: rgb(231, 216, 216);
}
.layui-nav-header-logo {
  height: 50px;
  width: 5%;
  top: 15px;
  position: absolute;
  left: 5%;
}
.questionnaire_list {
  height: 50px;
  width: 5%;
  top: 15px;
  position: absolute;
  left: 18%;
}
.personal_data {
  height: 50px;
  width: 5%;
  top: 15px;
  position: absolute;
  left: 24.5%;
}
.platform_statistics {
  height: 50px;
  width: 5%;
  top: 15px;
  position: absolute;
  left: 11.5%;
}
.setting {
  width: 3%;
  position: absolute;
  right: 1%;
  background: rgb(219, 208, 208);
  top: 18px;
}
.full {
  width: 3%;
  position: absolute;
  right: 5%;
  background: rgb(219, 208, 208);
  top: 18px;
}
.person_main {
  width: 100%;
  height: 95%;
  position: absolute;
  background: rgb(206, 203, 203);
  top: 20%;
}
.num {
  width: 5%;
  height: 40px;
  position: absolute;
  top: 20px;
  left: 31.5%;
}
.num1 {
  width: 6%;
  height: 40px;
  position: absolute;
  top: 15px;
  left: 35.5%;
}
.plat {
  width: 8%;
  height: 40px;
  position: absolute;
  top: 20px;
  left: 41%;
}
.plat1 {
  width: 6%;
  height: 40px;
  position: absolute;
  top: 15px;
  left: 31.5%;
}
.time {
  width: 8%;
  height: 40px;
  position: absolute;
  top: 20px;
  left: 69%;
}
.time1 {
  width: 8%;
  height: 40px;
  position: absolute;
  top: 10px;
  left: 74.5%;
}
.status {
  width: 8%;
  height: 40px;
  position: absolute;
  top: 20px;
  left: 52%;
}
.status1 {
  width: 11%;
  height: 40px;
  position: absolute;
  top: 15px;
  left: 57.5%;
}
.search_button1 {
  position: absolute;
  top: 15px;
  left: 98%;
}
.jiayin {
  width: 10%;
  height: 10%;
  position: absolute;
  top: 1%;
  left: 1%;
}
.search_class{
  position: absolute;
  top: 10%;
  width: 100%;
  left: -32%;
}
</style>