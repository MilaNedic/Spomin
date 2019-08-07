%rebase('base.tpl')
%import model
<h1>Spomin</h1>

<blockquote>
	<i>Spomin je najboljša igra za urjenje spomina ;).</i>
</blockquote>


<table>

    <tr>
		<td> Izberi težavnost: lahko=2, srednje=3, težko=4</td>
	</tr>
	
	<tr>
		<td>
			<form action="/nova_igra/" method="POST">
				tezavnost: <input type="text" name="tezavnost">
				<input type="submit" value="tezavnost">
			</form>
		</td>
	</tr>

	
</table>
