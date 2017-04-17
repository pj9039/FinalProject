<HTML>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<HEAD>
	<title>개미추적자</title>

    <!-- Bootstrap core CSS -->
    <link href="./css/bootstrap.min.css" rel="stylesheet">

    <script src="./js/bootstrap.min.js"></script>


<style type="text/css">
	th,td{padding: 15px;}
	table{border-spacing: 5px;}
	img:hover {
   padding:1px;
   border:1px solid #021a40;
   background-color:#ff0;
	}
	.activeImg{
		padding:1px;
   border:1px solid #021a40;
   background-color:#ff0;
	}
</style>
<script>
	function borderClick(bId){
			var img = document.getElementById(bId);

			for(var i = 1; i < 10; i++){
				var imgTmp = document.getElementById("img"+i);
				imgTmp.classList.remove("activeImg");
			}

			img.classList.add("activeImg");
	}
</script>
</HEAD>
<body>
<center>
	<BR>
	<H1>그래프검색</H1>
	<BR>
	<HR>
	<form action="P_result.php" method="post">
	<table style="width:1200">
		<tr>
			<th align="center"><font size="5"/><span class="glyphicon glyphicon-check"></span> 그래프</th>
			<th align="center"><font size="5"/><span class="glyphicon glyphicon-search"></span> 추가조건</th>
		</tr>
	</table>
	<!--tr:한줄 th:글씨 진하게 td:글씨보통 colspan:가로줄을 합치는 개수 rowspan:세로줄을 합치는 개수-->
	<div style="display:table">
	<div style="display:table-cell; text-align:center">
	<div style="width: 600px; height: 500px; border: 1px; float: left;">
	<table width="600" height="500" border="0" style="text-align: center;">
	<tr>
		<td>
			<a href="javascript:borderClick('img1')"><img id="img1" src="image/pattern1.PNG" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image1"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img2')"><img id="img2" src="image/pattern2.PNG" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image2"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img3')"><img id="img3" src="image/pattern3.PNG" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image3"/> -->
		</td>
	</tr>
	<tr>
		<td>
			<a href="javascript:borderClick('img4')"><img id="img4" src="image/pattern4.PNG" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image4"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img5')"><img id="img5" src="image/pattern5.PNG" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image5"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img6')"><img id="img6" src="image/pattern6.PNG" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image6"/> -->
		</td>
	</tr>
	<tr>
		<td>
			<a href="javascript:borderClick('img7')"><img id="img7" src="image/pattern7.PNG" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image7"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img8')"><img id="img8" src="image/pattern8.PNG" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image8"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img9')"><img id="img9" src="image/pattern9.PNG" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image9"/> -->
		</td>
	</tr>
</table>
	</div>
	<div style="position: relative; width: 600px; height: 500px; border: 1px;  float: left; display:table;">
	<div style="display:table-cell;vertical-align:middle;">
	<table width="600" height="500" border="0" text-align: center;">
	<tr style="vertical-align:bottom;">
		<td colspan="3" style="text-align:left;"><font size="5"><span class="glyphicon glyphicon-expand"></span> 가격</font></td>
	</tr>
	<tr style="vertical-align:top;">
		<td><input class="form-control" type=text name="price1" size="20" /></td>
		<td><font size="5"/> ~ </td>
		<td><input class="form-control" type=text name="price2" size="20"/></td>
	</tr>
</table>
</div>
</div>
</div>
</div>
<table style="width:1200">
	<tr>
		<td  style="word-spacing: 15px" align="center"><input type="submit" class="btn btn-default" style="width: 300px; height:50px" value=검색> </td>	
		<td  style="word-spacing: 15px" align="center"><input type="reset" class="btn btn-default" style="width: 300px; height: 50px" value=리셋> </td>
	</tr>
</table>
	</form>
</center>
</body>
</HTML>
