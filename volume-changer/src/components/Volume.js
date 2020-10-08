import React from "react";
import { AwesomeButton } from "react-awesome-button";
import { TiMinus, TiPlus } from "react-icons/ti";
import { Grid } from "semantic-ui-react";
import { handleKeyPress } from "../api";

export const Volume = () => {
	return (
		<Grid columns="equal">
			<Grid.Row>
				<Grid.Column>
					<AwesomeButton onPress={() => handleKeyPress("vol_up")}>
						<TiPlus size={20} />
					</AwesomeButton>
				</Grid.Column>
			</Grid.Row>
			<Grid.Row>
				<Grid.Column>
					<AwesomeButton onPress={() => handleKeyPress("vol_down")}>
						<TiMinus size={20} />
					</AwesomeButton>
				</Grid.Column>
			</Grid.Row>
		</Grid>
	);
};
