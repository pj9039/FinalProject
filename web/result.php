<!--DB 연동-->
<?
	$db = mysqli_connect("localhost","root","rla123","stock",9039);
	if(mysqli_connect_errno($db)){
		echo "연결실패 : ".mysqli_connect_error();
	} else {
		echo "성공";
	}
?>

<!--페이징 변수 정의-->
<?

	//select marketdate from stockprice order by marketdate desc limit 1;	//가장 최근 날짜 조회
	//select * from stockprice where marketdate='변수(2017-01-10)'
	//$shcode = $_POST['shcode'];
	
	// 검색 날짜 조건 설정
	$now_date = "SELECT marketdate from stockprice order by marketdate desc limit 1";
	// 가장 최근 날짜
	$date = mysqli_query($db,"SELECT marketdate from stockprice order by marketdate desc limit 1");
	$date_data = mysqli_fetch_row($date);
	$date_result = $date_data[0];


	$pageNum = ($_GET['page']) ? $_GET['page'] : 1;	//초기값 1로 지정
	$list = ($_GET['list']) ? $_GET['list'] : 5;	//한 페이지에 5개씩 보여주기
	$b_pageNum_list = 10;	//블록에 나타낼 페이지 번호 갯수
	$block = ceil($pageNum/$b_pageNum_list);	//현재 리스트의 블록을 구하는 식
	$b_start_page = (($block-1) * $b_pageNum_list) + 1;	//현재 블럭에서 시작페이지 번호
	$b_end_page = $b_start_page + $b_pageNum_list - 1;	//현재 블럭에서 마지막 페이지 번호
	$tot_count_query = mysqli_query($db,"SELECT count(*) FROM stockprice where marketdate='".$date_result."'");	//행의 개수
	$rows = mysqli_fetch_array($tot_count_query);
	$total_count = $rows[0];
	$total_page = ceil($total_count / $list);	//총 행의 페이지 수
	$total_block = ceil($total_page / $b_pageNum_list);	//block의 총 갯수
	$start_list = $list*($pageNum-1);	// 현재화면에서 시작 항목 번호


if ($b_end_page > $total_page){	//마지막 페이지가 총 페이지보다 클 때 같게 해주는 조건
		$b_end_page = $total_page;
	}

// 리스트 출력을 위한 쿼리
		$date_query = "SELECT * FROM stockprice where marketdate='".$date_result."' limit ".$start_list.", ".$list;
		
		// 가장 최근날짜 검색 결과
		$result = mysqli_query($db,$date_query);
		
?>
<HTML>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<HEAD>
	<title>개미추적자</title>

    <!-- Bootstrap core CSS -->
    <link href="./css/bootstrap.min.css" rel="stylesheet">

    <script src="./js/bootstrap.min.js"></script>

	<style type="text/css">
/*		table, td{
			border:1px;
		}
		table{
			width: 60%;
			height: 100px;
			margin: auto;
			text-align: center;
		}*/
	a:link { color: red; text-decoration: none;}
 	a:visited { color: black; text-decoration: none;}
 	a:hover { color: blue; text-decoration: underline;}
	</style>
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
			<a href="javascript:borderClick('img1')"><img id="img1" src="image/sample.png" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image1"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img2')"><img id="img2" src="image/sample.png" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image2"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img3')"><img id="img3" src="image/sample.png" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image3"/> -->
		</td>
	</tr>
	<tr>
		<td>
			<a href="javascript:borderClick('img4')"><img id="img4" src="image/sample.png" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image4"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img5')"><img id="img5" src="image/sample.png" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image5"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img6')"><img id="img6" src="image/sample.png" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image6"/> -->
		</td>
	</tr>
	<tr>
		<td>
			<a href="javascript:borderClick('img7')"><img id="img7" src="image/sample.png" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image7"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img8')"><img id="img8" src="image/sample.png" width="150" height="100"></a>
			<!-- <input type="checkbox" name="image8"/> -->
		</td>
		<td>
			<a href="javascript:borderClick('img9')"><img id="img9" src="image/sample.png" width="150" height="100"></a>
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
	<tr style="vertical-align:bottom;">
		<td colspan="3" style="text-align:left;"><font size="5"><span class="glyphicon glyphicon-expand"></span> ROE</font></td>
	</tr>
	<tr style="vertical-align:top;">
			<td> <input class="form-control" type=text name="roe1" size="20"/> </td>
			<td><font size="5"/> ~ </td>
			<td> <input class="form-control" type=text name="roe2" size="20" /> </td>
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

	<HR>
	<H2>검색결과</H2>
	<a href="graph.php">되돌아가기</a>
	<br><br><br>
		<!-- <table style="border:1px solid #bcbcbc;"> -->
		<table class="table" style="width:80%;">
		<tr style="background-color:#EAEAEA;border-bottom:2px solid black;border-top:2px solid black;">
			<th style="text-align:center;"><font size="5"/>번호</th>
			<th style="text-align:center;"><font size="5"/>종목코드</th>
			<th style="text-align:center;"><font size="5"/>날짜</th>
			<th style="text-align:center;"><font size="5"/>종가</th>
		</tr>

	<?
		if (mysqli_num_rows($result) > 0) {
    	// output data of each row
    	$i = 1;
			while($row = mysqli_fetch_assoc($result)) {
				if($i%2 == 0){
	?>
				<tr style="background-color:white;">
	<?
				} else {
	?>
					<tr>
	<?
				}
	?>
				
					<td style="border:1px solid #bcbcbc;"><a href="result.php"/><? echo $row["idx"] ?></a></td>
					<td style="border:1px solid #bcbcbc;"><? echo $row["shcode"] ?></td>
					<td style="border:1px solid #bcbcbc;"><? echo $row["marketdate"] ?></td>
					<td style="border:1px solid #bcbcbc;"><? echo $row["closeprice"] ?></td>
				</tr>
				<?
				$i++;
			}
		}
		?>
	</table>
	<table>
		<tr>
			<td>
<?//첫 페이지
	if($pageNum <= 1){?>
		<font size=2 color=red>[처음] </f ont>
	<?}else{?>
				<font size="2"><a href="P_result.php?page=&list=<?=$list?>" style="text-decoration:none">[처음] </a></font>
		<?}

	//거꾸로 가는 이전페이지
	if($block <= 1){?>
		<font> </font>
	<?}else{?>
			<font size="2"><a href="P_result.php?page=<?=$b_start_page-1?>&list=<?=$list?>" style="text-decoration:none">[이전] </a></font>
	<?}

		//페이징 번호
	for($j=$b_start_page; $j<=$b_end_page; $j++){
		if($pageNum==$j){?>
				<font size="2" color="red"><?=$j?> </font>
		<?}else{?>
					<font size="2"><a href="P_result.php?page=<?=$j?>&list=<?=$list?>" style="text-decoration:none"><?=$j?> </a></font>
		<?}
	}

	//다음 링크 버튼
	if($block>=$total_block){?>
		<font>  </font>
	<?}else{?>
				<font size="2"><a href="P_result.php?page=<?=$b_end_page+1?>&list=<?=$list?>" style="text-decoration:none">[다음] </a></font>
	<?}

	//마지막 링크 버튼
	if($pageNum >= $total_page){?>
		<font size="2" color="red">[마지막]</font>
	<?}else{?>
				<font size="2"><a href="P_result.php?page=<?=$total_page?>&list=<?=$list?>" style="text-decoration:none">[마지막]</a></font>
	<?}?>
			</td>
		</tr>
	</table>

	<?	//test.py실행시키고 test.png파일이 생성되고 test.png을 출력하기
		system('python3 /var/www/html/final/python/test.py');
		
	?>
	<h2>그래프</h2>
	<img src="test.png">
	</form>
</center>
</body>
</HTML>
