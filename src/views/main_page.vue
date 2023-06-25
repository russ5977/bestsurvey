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
      <div class="button_class">
        <div class="number">项目编号</div>
        <div class="number1">
          <el-input v-model="keyword" placeholder="项目编号"></el-input>
        </div>
        <div class="platform2">平台</div>
        <div class="platform3" style="margin-left: 15%">
          <el-input v-model="keyword" placeholder="平台"></el-input>
        </div>
        <div class="search_button">
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
  <div class="main">
    <el-table :data="houselist" border stripe>
      <el-table-column label="项目编号" prop="number"></el-table-column>
      <el-table-column label="项目名称" prop="introduction"></el-table-column>
      <el-table-column label="项目单价" prop="price"></el-table-column>
      <el-table-column label="国家地区" prop="country"></el-table-column>
      <el-table-column label="最低时长" prop="duration"></el-table-column>
      <el-table-column label=" 更新时间" prop="date"></el-table-column>
      <el-table-column label="项目操作">
        <div class="join">
          <el-button type="primary" round>进入调查</el-button>
        </div>
        <br />
        <div class="check">
          <el-button type="success" round>查看要求</el-button>
        </div>
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
      // :data=houselist
      houselist: [],
      alllist: [],
      username: localStorage.getItem("username"),
      keyword: "",
    };
  },
  methods: {
    //这是要展示的数据total
    get_house() {
      Axios.get("/main/show/")
        .then((resp) => {
          console.log("2222", resp.data);
          //这是把后端获取的分页数据传到houselist列表里面了
          this.houselist = resp.data.results;
          this.total = resp.data.count;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    show_all() {
      Axios.get("/main/show/")
        .then((resp) => {
          console.log("2222", resp.data);
          //这是把后端获取的分页数据传到houselist列表里面了
          this.alllist = resp.data.results;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    search_survey() {
      Axios.post("/main/search/", { keyword: this.keyword })
        .then((resp) => {
          console.log(resp.data);
          this.list1 = resp.data.data;
          console.log(">>>>>>>>>>>>this.list1", this.list1);
          // this.$router.push("/search_survey");
          this.$router.push({
            name: "search_survey",
            params: { keyword: this.keyword },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 监听 page size 改变的事件
    handleSizeChange(newSize) {
      this.queryInfo.pagesize = newSize;
      this.show_all();
    },

    // 监听 页码值 改变的事件
    handleCurrentChange(newPage) {
      this.queryInfo.pagenum = newPage;
      this.show_all();
    },
  },
  mounted() {
    this.get_house();
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
  left: 25%;
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
.main {
  width: 100%;
  height: 95%;
  position: absolute;
  background: rgb(206, 203, 203);
  top: 200px;
}
.search {
  width: 100%;
  height: 20%;
  position: absolute;
  background: rgb(254, 251, 251);
  top: 80px;
}
.number {
  width: 5%;
  height: 40px;
  position: absolute;
  top: 27px;
  left: 33%;
}
.number1 {
  width: 8%;
  height: 40px;
  position: absolute;
  top: 23px;
  left: 38%;
}
.platform2 {
  width: 8%;
  height: 40px;
  position: absolute;
  top: 26px;
  left: 44.5%;
}
.platform3 {
  width: 8%;
  height: 40px;
  position: absolute;
  top: 23px;
  left: 35.5%;
}
.search_button {
  position: absolute;
  top: 25px;
  left: 63%;
}
.jiayin {
  width: 10%;
  height: 10%;
  position: absolute;
  top: 2.5%;
  left: 1%;
}
.button_class {
  position: absolute;
  top: 12%;
  width: 100%;
  left: -32%;
}
</style>