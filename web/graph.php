<!--DB 연동-->
<?
	$db = mysqli_connect("pj9039.iptime.org:9039","root","rla123","stock");
	if(mysqli_connect_errno($db)){
		echo "연결실패 : ".mysqli_connect_error();
	} else {
		echo "성공";
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
	<form action="P_result.php" method="post">
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
			<td> <input type=text name=roe1/> </td>
			<td> < ROE < </td>
			<td> <input type=text name=roe2/> </td>
		</tr>

		<tr>
			<td>그래프7</td>
			<td>그래프8</td>
			<td>그래프9</td>
			<td colspan="3" style="word-spacing: 15px"> <input type=submit value=검색> <input type=reset value=리셋> </td>
		</tr>

		
	</table>


	</form>
</center>
</body>
</HTML>