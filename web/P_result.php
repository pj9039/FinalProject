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
	$pageNum = ($_GET['page']) ? $_GET['page'] : 1;	//초기값 1로 지정
	$list = ($_GET['list']) ? $_GET['list'] : 5;	//한 페이지에 5개씩 보여주기
	$b_pageNum_list = 10;	//블록에 나타낼 페이지 번호 갯수
	$block = ceil($pageNum/$b_pageNum_list);	//현재 리스트의 블록을 구하는 식
	$b_start_page = (($block-1) * $b_pageNum_list) + 1;	//현재 블럭에서 시작페이지 번호
	$b_end_page = $b_start_page + $b_pageNum_list - 1;	//현재 블럭에서 마지막 페이지 번호
	$tot_count_query = mysqli_query($db,"SELECT count(*) FROM stockprice");	//행의 개수
	$rows = mysqli_fetch_array($tot_count_query);
	$total_count = $rows[0];
	$total_page = ceil($total_count / $list);	//총 행의 페이지 수
	$total_block = ceil($total_page / $b_pageNum_list);	//block의 총 갯수
	$start_list = $list*($pageNum-1);	// 현재화면에서 시작 항목 번호

if ($b_end_page > $total_page){	//마지막 페이지가 총 페이지보다 클 때 같게 해주는 조건
		$b_end_page = $total_page;
	}
		
?>
<HTML>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<HEAD>
	<title>개미추적자</title>

	<style type="text/css">
		table, td{
			border:1px;
		}
		table{
			width: 60%;
			height: 100px;
			margin: auto;
			text-align: center;
		}
	a:link { color: red; text-decoration: none;}
 	a:visited { color: black; text-decoration: none;}
 	a:hover { color: blue; text-decoration: underline;}
	</style>
	
</HEAD>
<body>
<center>
	<BR>
	<H1>그래프검색</H1>
	<BR>
	<!--그래프검색-->
	<input type=button value=메인화면 onclick="location.href='main.php';"/><BR><BR>
	<HR>
	<form action="graph.php" method="post">
	<!--tr:한줄 th:글씨 진하게 td:글씨보통 colspan:가로줄을 합치는 개수 rowspan:세로줄을 합치는 개수-->
	<table border=0 cellpadding=5 cellspacing=1>
		<tr>
			<th colspan="3" align="left"><font size="5"/>그래프</th>
			<th colspan="3" align="left"><font size="5"/>추가조건</th>
		</tr>

		<tr>
			<td>그래프1</td>
			<td>그래프2</td>
			<td>그래프3</td>
			<td> <input type=text name=price1/> </td>
			<td> < 가격 < </td>
			<td> <input type=text name=price2/> </td>
		</tr>

		<tr>
			<td>그래프4</td>
			<td>그래프5</td>
			<td>그래프6</td>
			<td> <input type=text name=volume1/> </td>
			<td> < ROE < </td>
			<td> <input type=text name=volume2/> </td>
		</tr>

		<tr>
			<td>그래프7</td>
			<td>그래프8</td>
			<td>그래프9</td>
			<td colspan="3" style="word-spacing: 15px"> <input type="submit" value="검색"> <input type="reset" value="리셋"> </td>
		</tr>

	</table>

	<HR>
	<H2>검색결과</H2>
	<a href="graph.php">되돌아가기</a>
	<br><br><br>
		<table style="border:1px solid #bcbcbc;">
		<tr>
			<th><font size="5"/>번호</th>
			<th><font size="5"/>종목코드</th>
			<th><font size="5"/>날짜</th>
			<th><font size="5"/>종가</th>
		</tr>

		<tr>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
		</tr>

	<?
		//select marketdate from stockprice order by marketdate desc limit 1;	//가장 최근 날짜 조회
		//select * from stockprice where marketdate='변수(2017-01-10)'
		#$shcode = $_POST['shcode'];
		$result = mysqli_query($db,"SELECT * FROM stockprice limit 1".$start_list.", ".$list);
		if (mysqli_num_rows($result) > 0) {
    	// output data of each row
			while($row = mysqli_fetch_assoc($result)) {
				?>
				<tr>
					<td style="border:1px solid #bcbcbc;"><a href="result.php"/><? echo $row["idx"] ?></a></td>
					<td style="border:1px solid #bcbcbc;"><? echo $row["shcode"] ?></td>
					<td style="border:1px solid #bcbcbc;"><? echo $row["marketdate"] ?></td>
					<td style="border:1px solid #bcbcbc;"><? echo $row["closeprice"] ?></td>
				</tr>
				<?
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

	</form>
</center>
</body>
</HTML>

<!-- 
select marketdate from stockprice order by marketdate desc limit 1;	//가장 최근 날짜 조회
select * from stockprice where marketdate='변수(2017-01-10)'
종목코드 날짜 doesprice(종가)
-->